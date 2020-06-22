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
    template = loader.get_template('backend/index.html')

    return HttpResponse(template.render(serializer.data, request))

