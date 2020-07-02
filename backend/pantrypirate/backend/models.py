from django.db import models
from django.contrib.auth.models import User


class DietaryRequirement(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name


class MealCategory(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cook_time = models.CharField(max_length=50)
    method = models.CharField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="recipes")
    meal_cat = models.ManyToManyField(MealCategory,
                                      related_name="recipes", blank=True)
    diet_req = models.ManyToManyField(DietaryRequirement,
                                      related_name="recipes", blank=True)
    favourites = models.ManyToManyField(User, related_name="favourites",
                                        blank=True)

    def __str__(self):
        return self.name


class IngredientCategory(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    category = models.ForeignKey(IngredientCategory,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    adjective = models.CharField(max_length=30, blank=True, null=True)
    unit = models.CharField(max_length=20)
    amount = models.CharField(max_length=5)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name="ingredients")

    def __str__(self):
        return self.ingredient.name


class PantryIngredient(models.Model):
    expiry_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient.name

