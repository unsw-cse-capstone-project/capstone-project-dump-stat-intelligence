from rest_framework import viewsets
from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('name')
    serializer_class = RecipeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all().order_by('name')
    serializer_class = IngredientSerializer


class PantryIngredientViewSet(viewsets.ModelViewSet):
    queryset = PantryIngredient.objects.all().order_by('name')
    serializer_class = PantryIngredientSerializer

