from rest_framework import viewsets
<<<<<<< HEAD
from rest_framework.authentication import TokenAuthentication, \
    SessionAuthentication, BaseAuthentication
=======
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication,
)
>>>>>>> ef89d035f1f970b67b3416ac63738a20bc7cae91
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from rest_framework.views import Response, Http404
import json


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-id")
    serializer_class = UserSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by("name")
    serializer_class = RecipeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all().order_by("name")
    serializer_class = IngredientSerializer


class PantryIngredientViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication,
                              BaseAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PantryIngredient.objects.all().order_by('ingredient')
    serializer_class = PantryIngredientSerializer

    def list(self, request, *args, **kwargs):
        queryset = PantryIngredient.objects.filter(
            user=request.user).order_by('ingredient')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

