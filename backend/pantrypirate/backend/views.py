from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .serializers import *
from .models import *
from rest_framework.views import Response
import json

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
    authentication_classes = [TokenAuthentication]
    queryset = PantryIngredient.objects.all().order_by('ingredient')
    serializer_class = PantryIngredientSerializer

    def list(self, request, *args, **kwargs):
        queryset = PantryIngredient.objects.filter(
            user=request.user).order_by('ingredient')
        serializer = self.get_serializer(queryset, many=True)
        return Response(json.dumps(serializer.data))

