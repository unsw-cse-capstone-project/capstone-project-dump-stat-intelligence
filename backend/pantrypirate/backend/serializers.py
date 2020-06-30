# REST serialisers
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'favourites']
        extra_kwargs = {'favourites' : {'required' : False}}


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
        fields = ['id', 'username']


class IngredientCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = IngredientCategory
        fields = ['name']
        extra_kwargs = {
            'name' : {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class IngredientSerializer(serializers.ModelSerializer):
    category = IngredientCategorySerializer()

    class Meta:
        model = Ingredient
        fields = ['name', 'category']

    def create(self, validated_data):
        cat_data = validated_data.pop('category')
        cat, _ = IngredientCategory.objects.get_or_create(**cat_data)
        return Ingredient.objects.create(**validated_data, category=cat)

    def update(self, instance, validated_data):
        cat_data = validated_data.pop('category')
        cat, _ = IngredientCategory.objects.get_or_create(**cat_data)
        instance.name = validated_data.get('name', instance.name)
        instance.category = cat
        instance.save()
        return instance


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ['adjective', 'unit', 'amount', 'recipe', 'ingredient']
        extra_kwargs = {'adjective' : {'required' : False}}
        read_only_fields = ['recipe']


class RecipeSerializer(serializers.ModelSerializer):
    meal_cat = MealCatSerializer(many=True)
    diet_req = DietReqSerializer(many=True)
    favourites = FavouritesSerializer(many=True)
    ingredients = RecipeIngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'cook_time', 'method', 'author', 'meal_cat',
                  'diet_req', 'favourites', 'ingredients']
        extra_kwargs = {'favourites' : {'required' : False},
                        'meal_cat' : {'required' : False},
                        'diet_req' : {'required' : False}}

    def create(self, validated_data):
        print(validated_data)
        recipe_ing_data = validated_data.pop('ingredients')
        fav = validated_data.pop('favourites')
        diet_req = validated_data.pop('diet_req')
        meal_cat = validated_data.pop('meal_cat')
        print(meal_cat)
        recipe = Recipe.objects.create(**validated_data)
        for cat in meal_cat:
            recipe.meal_cat.set(cat['name'])

        return recipe

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['author'] = UserSerializer(instance.author).data
        return response


class PantryIngredientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    ingredient = IngredientSerializer()

    class Meta:
        model = PantryIngredient
        fields = ['expiry_date', 'user', 'ingredient']
        extra_kwargs = {'expiry_date' : {'required' : False}}