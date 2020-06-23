from django.http import JsonResponse
from .serializers import *
from .models import *


# Extract list of dict values
def extract_values(x, key):
    out = []
    for y in x:
        out.append(y.get(key))
    return out


# Recipe view
def recipe(request, recipe_id):
    # Extract recipe with id and serialise
    recipe = Recipe.objects.get(pk=recipe_id)
    serializer = RecipeSerializer(instance=recipe)

    # Take serialise dump and extract out name fields for meal category and
    # dietary requirements
    data = serializer.data
    data["author"] = recipe.author.name
    data["meal_cat"] = extract_values(data["meal_cat"], "name")
    data["diet_req"] = extract_values(data["diet_req"], "name")
    data["favourites"] = extract_values(data["favourites"], "name")

    return JsonResponse(data)
