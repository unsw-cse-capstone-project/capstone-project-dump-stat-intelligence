from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def example(request):
    return JsonResponse({'hello' : 'world'})