from django.db import models
from django.contrib.auth.models import User

'''
    Models for website
'''

# Meta data for search queries
class MetaSearch(models.Model):
    search = models.CharField(max_length=200, primary_key=True)
    references = models.IntegerField(default=0)


# Name is primary key string
class DietaryRequirement(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name


# Name is primary key string
class MealCategory(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name


# Recipe contains required author field, and optional meal category, dietary
# requirement and favourites fields
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cook_time = models.CharField(max_length=50)
    method = models.CharField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="recipes")
    image_URL = models.CharField(max_length=200, blank=True, null=True)
    meal_cat = models.ManyToManyField(MealCategory,
                                      related_name="recipes", blank=True)
    diet_req = models.ManyToManyField(DietaryRequirement,
                                      related_name="recipes", blank=True)
    favourites = models.ManyToManyField(User, related_name="favourites",
                                        blank=True)

    def __str__(self):
        return self.name


# Name is primary key string
class IngredientCategory(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


# Name is primary key, required category
class Ingredient(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    category = models.ForeignKey(IngredientCategory,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Adjective field not required, ingredient foreign key will be a string,
# recipe foreign key will be an id integer
class RecipeIngredient(models.Model):
    adjective = models.CharField(max_length=30, blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)
    amount = models.CharField(max_length=5)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name="ingredients")

    def __str__(self):
        return self.ingredient.name


# Expiry date is optional, could have expiry status calculated here or higher up
# User foreign key will be an id integer, ingredient will be a string
class PantryIngredient(models.Model):
    expiry_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient.name

