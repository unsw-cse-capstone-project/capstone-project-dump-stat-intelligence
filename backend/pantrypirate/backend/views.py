from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import *
#from django.forms.models import model_to_dict
from django.template import loader
from django.core import serializers

# Create your views here.
def example(request):
    return JsonResponse({'hello' : 'world'})

def recipe(request, recipe_id):

    recipe = Recipe.objects.get(pk=recipe_id)
    serializer = RecipeSerializer(instance=recipe)
    
    # data = {'name': recipe.name, 'cook_time': recipe.cook_time, 
    #         'method': recipe.method, 'author': recipe_id.author.name,
    #         'meal_cat': recipe_id.meal_cat.name}

    return JsonResponse(serializer.data)