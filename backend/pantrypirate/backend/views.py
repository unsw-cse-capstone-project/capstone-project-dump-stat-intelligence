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
import json


# Custom token authentication to allow the id to be returned alongside the token
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


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
        if self.action is 'list':
            self.permission_classes = [IsAdminUser]
        return super(UserViewSet, self).get_permissions()

    # Make deletion only compatible for our account
    def destroy(self, request, *args, **kwargs):
        user_id = int([i for i in str(request.META['PATH_INFO']).split('/') if
                       i][
                          -1])
        if request.user.id is user_id:
            return super(UserViewSet, self).destroy(self, request, *args,
                                                  **kwargs)
        else:
            return Response(status=401)

    def partial_update(self, request, *args, **kwargs):
        user_id = int([i for i in str(request.META['PATH_INFO']).split('/') if
                       i][
                          -1])
        if request.user.id is user_id:
            return super(UserViewSet, self).update(self, request, *args, **kwargs)
        else:
            return Response(status=401)


# Register user, checks for duplicates
# Requires email, password and username, anyone can create account
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all().order_by("-id")
    serializer_class = CreateUser
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                authenticate(username=request.data['username'],
                             password=request.data['password'])
                token, created = Token.objects.get_or_create(user=user)
                data = serializer.data
                data['token'] = token.key
                return Response(data=data)
        return Response(serializer.errors, status=404)


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
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    # Search for recipes given the running list input and filters
    def list(self, request, *args, **kwargs):
        # looks like: meal=dinner+lunch&diet=vegan&limit=10&offset=21
        # print(request.GET.get('meal'))

        string = urllib.parse.parse_qs(request.META['QUERY_STRING'],
                                       keep_blank_values=True)
        # print(string)
        if not string:
            queryset = Recipe.objects.all().order_by('name')
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        meals = string['meal'][0].split()
        diets = string['diet'][0].split()
        running_list = string['ingredients'][0].split()
        # print(running_list)

        recipes = Recipe.objects.none()
        for item in running_list:
            # print(item)
            pIngredient = PantryIngredient.objects.get(pk=item)
            ingredient = pIngredient.ingredient
            for rec_ingredient in RecipeIngredient.objects.filter(
                    ingredient=ingredient):
                name = rec_ingredient.recipe
                recipes |= Recipe.objects.filter(name=name)

        f = recipes.distinct()

        # filter by dietary requirement (AND relationship)
        if len(diets) != 0:
            for requirement in diets:
                f = f.filter(diet_req__pk=requirement)

        # filter by meal category (OR relationship)
        e = Recipe.objects.none()
        if len(meals) != 0:
            for category in meals:
                e |= f.filter(meal_cat__pk=category)

        else:
            e = f  # if no meal categories specified, return all recipes

        # remove duplicates
        e = e.distinct()

        # temporarily returning list of matching recipe names
        lst = []
        for it in e:
            lst.append(it.name)

        return Response(lst)


# Supports create, retrieve, put, list and delete
# Refer to serialiser or test for format
class IngredientViewSet(viewsets.ModelViewSet):
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
            queryset = PantryIngredient.objects.filter(
                user=request.user).order_by('ingredient__category__name',
                'ingredient__name')
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(status=404)