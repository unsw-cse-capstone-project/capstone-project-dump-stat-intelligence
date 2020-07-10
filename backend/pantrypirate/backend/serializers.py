# REST serialisers
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "favourites"]
        extra_kwargs = {"favourites": {"required": False},
                        "password" : {"write_only" : True}}


class LoginUser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {"username": {"validators": [UnicodeUsernameValidator()]},
                        "password" : {"validators": [UnicodeUsernameValidator()]}}

    def to_representation(self, instance):
        return instance['id']


class CreateUser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response.pop('password')
        return response


class MealCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategory
        fields = ["name"]
        extra_kwargs = {"name": {"validators": [UnicodeUsernameValidator()],}}


class DietReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietaryRequirement
        fields = ["name"]
        extra_kwargs = {"name": {"validators": [UnicodeUsernameValidator()],}}


class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class IngredientCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientCategory
        fields = ["name"]
        extra_kwargs = {"name": {"validators": [UnicodeUsernameValidator()],}}


class IngredientSerializer(serializers.ModelSerializer):
    category = IngredientCategorySerializer()

    class Meta:
        model = Ingredient
        fields = ["name", "category"]
        extra_kwargs = {"name": {"validators": [UnicodeUsernameValidator()],}}

    def create(self, validated_data):
        cat_data = validated_data.pop("category")
        cat, _ = IngredientCategory.objects.get_or_create(**cat_data)
        return Ingredient.objects.create(**validated_data, category=cat)

    def update(self, instance, validated_data):
        cat_data = validated_data.pop("category")
        cat, _ = IngredientCategory.objects.get_or_create(**cat_data)
        instance.name = validated_data.get("name", instance.name)
        instance.category = cat
        instance.save()
        return instance


class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = ["adjective", "unit", "amount", "recipe", "ingredient"]
        extra_kwargs = {"adjective": {"required": False}}
        read_only_fields = ["recipe"]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["ingredient"] = IngredientSerializer(instance.ingredient).data
        return response


class RecipeSerializer(serializers.ModelSerializer):
    meal_cat = MealCatSerializer(many=True)
    diet_req = DietReqSerializer(many=True)
    ingredients = RecipeIngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = [
            "id",
            "name",
            "cook_time",
            "method",
            "author",
            "meal_cat",
            "diet_req",
            "favourites",
            "ingredients",
        ]
        extra_kwargs = {
            "favourites": {"required": False},
            "meal_cat": {"required": False},
            "diet_req": {"required": False},
        }

    def create(self, validated_data):
        recipe_ing_data = validated_data.pop("ingredients", [])
        # fav = validated_data.pop("favourites") # Idk what favourites are for but it is buggering the frontend
        # Favourites are the users who favourite the recipes, currently not
        # really implemented but should be sent in the post as empty list
        diet_req = validated_data.pop("diet_req", [])
        meal_cat = validated_data.pop("meal_cat", [])
        recipe = Recipe.objects.create(**validated_data)
        for diet_data in diet_req:
            cat = DietaryRequirement.objects.get(name=diet_data.get("name"))
            recipe.diet_req.add(cat)
        for cat_data in meal_cat:
            cat = MealCategory.objects.get(name=cat_data.get("name"))
            recipe.meal_cat.add(cat)
        for ing_data in recipe_ing_data:
            ing_data["recipe"] = recipe
            ing_data["ingredient"] = Ingredient.objects.get(
                name=ing_data.get("ingredient")
            )
            ing = RecipeIngredient.objects.create(**ing_data)
            recipe.ingredients.add(ing)

        recipe.save()
        return recipe

    def update(self, instance, validated_data):
        ingredients = validated_data.pop("ingredients", [])
        diet_req = validated_data.pop("diet_req", [])
        meal_cat = validated_data.pop("meal_cat", [])

        instance.name = validated_data.get("name", instance.name)
        instance.cook_time = validated_data.get("cook_time", instance.cook_time)
        instance.method = validated_data.get("method", instance.method)
        instance.author = validated_data.get("author", instance.author)

        # Remove ingredients that currently exist
        instance.diet_req.clear()
        instance.meal_cat.clear()
        ings = RecipeIngredient.objects.all().filter(recipe=instance.id)
        ings.delete()

        for diet_data in diet_req:
            req = DietaryRequirement.objects.get(name=diet_data.get("name"))
            instance.diet_req.add(req)

        for meal_data in meal_cat:
            cat = MealCategory.objects.get(name=meal_data.get("name"))
            instance.meal_cat.add(cat)

        # TODO: Understand what is going on here
        # Why does it only update if a ingredient id is returned
        # When are these ingredient ids returned to the frontend?
        # ----- Response
        # The else case creates new ingredients (adding to the recipe for
        # example).
        for ing in ingredients:
            ing_id = ing.get("id", None)
            if ing_id:
                ingredient = RecipeIngredient.objects.get(id=ing_id, recipe=instance)
                ingredient.adjective = ing.get("adjective", ing.adjective)
                ingredient.unit = ing.get("unit", ing.unit)
                ingredient.amount = ing.get("amount", ing.amount)
                ingredient.ingredient = ing.get("ingredient", ing.ingredient)
                ingredient.save()

            else:
                ing["recipe"] = instance
                ing["ingredient"] = Ingredient.objects.get(name=ing.get("ingredient"))
                ing = RecipeIngredient.objects.create(**ing)
                instance.ingredients.add(ing)

        instance.save()
        return instance

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["author"] = UserSerializer(instance.author).data
        return response


class PantryIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PantryIngredient
        fields = ["id", "expiry_date", "user", "ingredient"]
        extra_kwargs = {"expiry_date": {"required": False}}

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["ingredient"] = IngredientSerializer(instance.ingredient).data
        response["user"] = UserSerializer(instance.user).data
        return response
