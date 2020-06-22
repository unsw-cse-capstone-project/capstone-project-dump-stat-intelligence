from django.db import models
from django.utils import timezone

import datetime


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class DietaryRequirement(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class MealCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    readonly_fields=('id',)
    name = models.CharField(max_length=50)
    cook_time = models.CharField(max_length=50)
    method = models.CharField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="author_recipe")
    favourite = models.ManyToManyField(User, related_name="favourite_recipe", blank=True)
    diet_req = models.ManyToManyField(DietaryRequirement, blank=True)
    meal_cat = models.ManyToManyField(MealCategory)

    def __str__(self):
        return self.name


class IngredientCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(IngredientCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    adjective = models.CharField(max_length=30)
    unit = models.CharField(max_length=20)
    amount = models.CharField(max_length=5)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient.name


class PantryIngredient(models.Model):
    expiry_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient.name

