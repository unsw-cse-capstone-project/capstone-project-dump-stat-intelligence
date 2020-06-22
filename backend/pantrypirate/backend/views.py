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
    #cat = serializers.serialize('json', Recipe.objects.get(pk=1))

    recipe = Recipe.objects.get(pk=1)

    # data = {'name': recipe_id.name, 'cook_time': recipe_id.cook_time, 
    #         'method': recipe_id.method, 'author': recipe_id.author.name,
    #         'favourite': recipe_id.favourite.name, 'diet_req': recipe_id.diet_req.name,
    #         'meal_cat': recipe_id.meal_cat.name}

    template = loader.get_template('backend/index.html')
    context = {'name': recipe.name, 'cook_time': recipe.cook_time, 'author': recipe.author,
               'method': recipe.method, 'favourite': recipe.favourite, 
               'diet_req': recipe.diet_req.name, 'meal_cat': recipe.meal_cat.name}

    return HttpResponse(template.render(context,request))