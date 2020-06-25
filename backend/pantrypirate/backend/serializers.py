# Serialisers for converting models to JSON
from rest_framework import serializers
from .models import *


class MealCatSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealCategory
        fields = ['name']


class DietReqSerializer(serializers.ModelSerializer):

    class Meta:
        model = DietaryRequirement
        fields = ['name']


class FavouritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name']


class RecipeSerializer(serializers.ModelSerializer):
    meal_cat = MealCatSerializer(many=True, read_only=True)
    diet_req = DietReqSerializer(many=True, read_only=True)
    favourites = FavouritesSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['name', 'cook_time', 'method', 'author', 'meal_cat',
                  'diet_req', 'favourites']