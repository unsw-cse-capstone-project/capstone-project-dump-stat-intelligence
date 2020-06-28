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


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['name', 'category']


class IngredientCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = IngredientCategory
        fields = ['name']


class RecipeIngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeIngredient
        fields = ['adjective', 'unit', 'amount', 'ingredient']


class RecipeSerializer(serializers.ModelSerializer):
    meal_cat = MealCatSerializer(many=True, read_only=True)
    diet_req = DietReqSerializer(many=True, read_only=True)
    favourites = FavouritesSerializer(many=True, read_only=True)
    ingredients = RecipeIngredientSerializer(source="recipeingredient_set",
                                             many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['name', 'cook_time', 'method', 'author', 'meal_cat',
                  'diet_req', 'favourites', 'ingredients']