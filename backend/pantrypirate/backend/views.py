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

    template = loader.get_template('polls/index.html')
    context = {}

    recipe_id = Recipe.objects.get(pk=1)

    data = {'name': recipe_id.name, 'cook_time': recipe_id.cook_time, 
            'method': recipe_id.method, 'author': recipe_id.author.name,
            'favourite': recipe_id.favourite.name, 'diet_req': recipe_id.diet_req.name,
            'meal_cat': recipe_id.meal_cat.name}

    return JsonResponse(data)