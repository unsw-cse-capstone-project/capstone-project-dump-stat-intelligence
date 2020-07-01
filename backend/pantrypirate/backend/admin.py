from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(MealCategory)
admin.site.register(DietaryRequirement)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(PantryIngredient)
admin.site.register(IngredientCategory)
