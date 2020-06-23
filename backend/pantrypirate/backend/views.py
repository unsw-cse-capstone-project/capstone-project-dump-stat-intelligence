from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import *
#from django.forms.models import model_to_dict
from django.template import loader
from django.core import serializers
import json

# Create your views here.
def example(request):
    return JsonResponse({'hello' : 'world'})


# Recipe view
def recipe(request, recipe_id):
    # Extract recipe with id and serialise
    recipe = Recipe.objects.get(pk=recipe_id)
    serializer = RecipeSerializer(instance=recipe)

    # Take serialise dump and extract out name fields for meal category and
    # dietary requirements
    data = serializer.data
    temp = data["meal_cat"]
    out = []
    for x in temp:
        out.append(x.get("name"))
    data["meal_cat"] = out

    return JsonResponse(data, safe=False)

