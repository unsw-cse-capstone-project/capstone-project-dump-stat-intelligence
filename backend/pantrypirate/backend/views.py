from rest_framework import viewsets, generics, views
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import *
from .models import *
from rest_framework.views import Response, Http404
import urllib.parse


# Allows updating of the user accounts, can get a list of all users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-id")
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action is 'list':
            self.permission_classes = [IsAdminUser]
        return super(UserViewSet, self).get_permissions()


# Register user, checks for duplicates
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
                return Response(data=serializer.data)
        return Response(serializer.errors, status=404)


# Removes the authentication token from the user, logging them out
class UserLogout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


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


class IngredientViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Ingredient.objects.all().order_by("name")
    serializer_class = IngredientSerializer


class PantryIngredientViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
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