from rest_framework import viewsets, generics, views
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import *
from .models import *
from rest_framework.views import Response, Http404
import urllib.parse
from django.contrib.auth import authenticate
from django.db.models import Max
import json
from collections import Counter


# View that requests the most commonly searched ingredient queries, maximum 3
# ingredients
class MetaSearchView(generics.ListAPIView):
    serializer_class = MetaSerializer

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            result = MetaSearch.objects.all().order_by("-references")
            if not result:
                return Response(data={'search': 'No searches have been made '
                                                'yet', 'references': 0})
            serializer = self.get_serializer(result[0])
            return Response(serializer.data)
        else:
            return Response(status=401)


# Custom token authentication to allow the id to be returned alongside the token
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response({"token": token.key, "id": token.user_id})


# Allows updating of the user accounts, can get a list of all users
# Default permission class is authenticated with the exception of list.
# However, additional changes will need to be made to permissions and
# detection based on frontend requirements
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-id")
    serializer_class = UserSerializer

    # Currently, user list is set to admin only access so that users cannot
    # get a list of users. If needed I can change.
    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [IsAdminUser]
        return super(UserViewSet, self).get_permissions()

    # Make deletion only compatible for our account
    def destroy(self, request, *args, **kwargs):
        user_id = int([i for i in str(request.META["PATH_INFO"]).split("/") if i][-1])
        if request.user.id is user_id:
            return super(UserViewSet, self).destroy(request, *args, **kwargs)
        else:
            return Response(status=401)

    # Make partial_update
    def partial_update(self, request, *args, **kwargs):
        user_id = int([i for i in str(request.META["PATH_INFO"]).split("/") if i][-1])
        if request.user.id is user_id:
            return super(UserViewSet, self).partial_update(request, *args, **kwargs)
        else:
            return Response(status=401)

    def update(self, request, *args, **kwargs):
        user_id = int([i for i in str(request.META["PATH_INFO"]).split("/") if i][-1])
        if request.user.id is user_id:
            return super(UserViewSet, self).update(request, *args, **kwargs)
        else:
            return Response(status=401)


# Register user, checks for duplicates
# Requires email, password and username, anyone can create account
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all().order_by("-id")
    serializer_class = CreateUser
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response(status=401)
        serializer = self.get_serializer
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                authenticate(
                    username=request.data["username"], password=request.data["password"]
                )
                token, created = Token.objects.get_or_create(user=user)
                data = serializer.data
                data["token"] = token.key
                return Response(data=data)
        return Response(serializer.errors, status=403)


# Removes the authentication token from the user, logging them out
# This solution currently does not have token expiration based on time,
# will need to be updated to account for it later
class UserLogout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# Recipes can be retrieved, updated, searched, deleted and created.
# Default permission is authenticated, currently doesn't check that the
# request user is the same as the update/delete recipe user, will need to be
# implemented later.
# Listing and retrieving can be done by any user
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by("name")
    serializer_class = RecipeSerializer

    # Make general and specific recipe get anonymous allowable
    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    # Search for recipes given the running list input and filters
    def list(self, request, *args, **kwargs):
        # query string looks like: meal=dinner+lunch&diet=vegan&limit=10&offset=21

        # Parse the query string
        string = urllib.parse.parse_qs(
            request.META["QUERY_STRING"], keep_blank_values=True
        )

        # If the query string does not exist, order by name and return
        if not string:
            queryset = Recipe.objects.all().order_by("name")
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        # Otherwise, filtering of some kind must occur so we create an empty
        # queryset
        recipes = Recipe.objects.none()

        # Check if ingredients were provided, if so filter based on matching,
        # otherwise take all recipes
        if string.get("ingredients")[0] is not "" or None:
            running_list = string["ingredients"][0].split(",")

            # For each ingredient, add recipes that contain it to the queryset
            for item in running_list:
                ingredient = Ingredient.objects.get(pk=item)
                for rec_ingredient in RecipeIngredient.objects.filter(
                    ingredient=ingredient
                ):
                    name = rec_ingredient.recipe
                    recipes |= Recipe.objects.filter(name=name)
        else:
            recipes = Recipe.objects.all().order_by("name")
            running_list = []

        # Remove duplicate recipes from the queryset
        f = recipes.distinct()

        # Check if dietary requirements were provided, if so filter based on
        # matching
        if string.get("diet") is not "" or None:
            diets = string["diet"][0].split()

            # Filter the queryset by dietary requirement (AND relationship)
            if len(diets) != 0:
                for requirement in diets:
                    f = f.filter(diet_req__pk=requirement)

        # Check if meal categories were provided, if so filter based on matching
        if string.get("meal") is not "" or None:
            meals = string["meal"][0].split()

            if len(meals) != 0:
                e = (
                    Recipe.objects.none()
                )  # need an empty set to build OR relationship from
                for category in meals:
                    e |= f.filter(meal_cat__pk=category)
                f = e  # rename back to f

        # remove duplicates
        f = f.distinct()

        # return matching recipes with the ingredients each recipe is missing
        # recipes returned in descending order of match %
        # then alphabetically
        # LAST element in response is suggested ingredient for user to add to their running list

        # return looks like:
        #   [{"recipe1" : OrderedDict(), "match_percentage" : num, "missing_ing" : ["ing1_name", "ing2_name"]},
        #    {"recipe2" : ...}
        #        .....
        #    {"suggestion" : "ing_name"}]

        f = f.order_by("name")
        recipe_list = self.get_serializer(f, many=True).data  # serialise so that recipe info can be returned later
        unordered_results = []

        all_missing_ingredients = []

        for rec in recipe_list:
            matching_ingredients = 0
            missing_ingredients = []

            for ing in Recipe.objects.get(pk=rec["id"]).ingredients.all():
                if ing.ingredient.name in running_list:
                    matching_ingredients += 1
                else:
                    missing_ingredients.append(ing.ingredient.name)
                    all_missing_ingredients.append(ing.ingredient.name)

            match_percentage = matching_ingredients / len(
                Recipe.objects.get(pk=rec["id"]).ingredients.all()
            )
            new_dict = {
                "recipe": rec,
                "match_percentage": match_percentage,
                "missing_ing": missing_ingredients,
            }
            unordered_results.append(new_dict)

        ordered_results = sorted(unordered_results, key=lambda k: k['match_percentage'], reverse=True)

        # now find ingredient to suggest
        # by default --> take most common unmatched ingredient amongst top 10 matching recipes
        # if user is logged in --> look through pantry ingredients first
        # suggest ingredient not in pantry only if there are no suitable pantry ingredients
        count = Counter(all_missing_ingredients)

        suggested_ingredient = None

        if count.most_common(1):
            suggested_ingredient = count.most_common(1)[0][0] # most common ingredient by default

        # from pantry if user is logged in
        if request.user.is_authenticated:
            # search through pantry
            found = False
            for missing_ing in count.most_common():
                if not found:
                    for pantry_ing in PantryIngredient.objects.filter(user=request.user):
                        if pantry_ing.ingredient.name == missing_ing[0]:
                            suggested_ingredient = missing_ing[0]
                            found = True
                            break

        # if somehow no ingredient was found then make it first ingredient not in running list
        if not suggested_ingredient:
            suggest = Ingredient.objects.exclude(name__in=running_list)
            if len(suggest) > 0:
                suggested_ingredient = suggest[0].name

        # if somehow still no ingredient was found then return empty string
        if not suggested_ingredient:
            suggested_ingredient = ""

        # add to return
        final_return = ordered_results.copy()
        final_return.append({"suggestion" : suggested_ingredient})

        # Update query string based on whether a match has been found
        full_match = 0
        if len(ordered_results) > 0 and ordered_results[0]["match_percentage"] == 1.0:
            full_match = 1
        self.update_search(string, full_match=full_match)

        return Response(final_return)

    # Takes boolean for full match and ingredients string from running list
    # input
    def update_search(self, list_string, full_match):
        # Update meta search model for query
        running_list = sorted(list_string["ingredients"][0].split(","))
        if 3 >= len(running_list) and '' not in running_list:
            running_list = "|".join(running_list)
            search = MetaSearch.objects.get_or_create(search=running_list)
            if not full_match:
                search[0].references += 1
            elif search[0].references > 0:
                search[0].references = 0
            search[0].save()


# Supports create, retrieve, put, list and delete
# Refer to serialiser or test for format
class IngredientViewSet(viewsets.ModelViewSet):
    pagination_class = None
    permission_classes = (IsAuthenticated,)
    queryset = Ingredient.objects.all().order_by("name")
    serializer_class = IngredientSerializer


# List currently has specific authentication request, likely redundant now
# that IsAuthenticated is the default permission for all views
# List returns ordered by category name primarily, then ingredient name
# secondarily
class PantryIngredientViewSet(viewsets.ModelViewSet):
    queryset = PantryIngredient.objects.all()
    serializer_class = PantryIngredientSerializer

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            queryset = PantryIngredient.objects.filter(user=request.user).order_by(
                "ingredient__category__name", "ingredient__name"
            )
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(status=404)

    # Make deletion only compatible for our account
    def destroy(self, request, *args, **kwargs):
        user_id = int([i for i in str(request.META["PATH_INFO"]).split("/") if i][-1])
        if request.user.id is user_id:
            return super(PantryIngredientViewSet, self).destroy(
                request, *args, **kwargs
            )
        else:
            return Response(status=401)

    # Make partial_update
    def partial_update(self, request, *args, **kwargs):
        user_id = int([i for i in str(request.META["PATH_INFO"]).split("/") if i][-1])
        if request.user.id is user_id:
            return super(PantryIngredientViewSet, self).partial_update(
                request, *args, **kwargs
            )
        else:
            return Response(status=401)

    def update(self, request, *args, **kwargs):
        user_id = int([i for i in str(request.META["PATH_INFO"]).split("/") if i][-1])
        if request.user.id is user_id:
            return super(PantryIngredientViewSet, self).update(request, *args, **kwargs)
        else:
            return Response(status=401)


class CookbookViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            queryset = Recipe.objects.filter(favourites=request.user.id)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(401)

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = User.objects.get(pk=request.user.id)
            user.favourites.add(request.data["id"])
            return Response(200)
        else:
            return Response(401)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = User.objects.get(pk=request.user.id)
            recipe_id = int(
                [i for i in str(request.META["PATH_INFO"]).split("/") if i][-1]
            )
            user.favourites.remove(recipe_id)
            return Response(200)
        else:
            return Response(401)


class MyRecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            queryset = Recipe.objects.filter(author=request.user.id)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(Http404)
