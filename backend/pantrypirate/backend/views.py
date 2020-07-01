from rest_framework import viewsets
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BaseAuthentication,
)
from django.db.models import Prefetch
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from .models import *
from rest_framework.views import Response, Http404
import urllib.parse
import json


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-id")
    serializer_class = UserSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by("name")
    serializer_class = RecipeSerializer

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

        running_list = json.loads(request.META['header'])
        # print(running_list)

        recipes = Recipe.objects.none()
        for item in running_list.values():
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
    queryset = Ingredient.objects.all().order_by("name")
    serializer_class = IngredientSerializer


class PantryIngredientViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = PantryIngredient.objects.all()
    serializer_class = PantryIngredientSerializer

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            queryset = PantryIngredient.objects.filter(
                user=request.user).order_by('ingredient__category__name',
                'ingredient__name')
            # print(queryset)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Http404