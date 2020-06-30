from django.urls import path
from .views import *

urlpatterns = [
    #path('', views.login, name='login'),
    path('user/<int:user_id>/', user, name = 'user'),
    #path('/user/{user_id}/cookbook', views.cookbook, name = 'cookbook'),
    path('ingredients/<str:ingredient_name>/', ingredients, name =
    'get_ingredient'),
    path('ingredients/', ingredients, name = 'set_get_ingredients'),
    path('user/<int:user_id>/pantry/', pantry, name = 'pantry'),
    path('user/<int:user_id>/pantry/<int:ingredient_id>', pantry, name =
    'delete_ingredient'),
    #path('/user/{user_id}/pantry/{ingredientId}', views.pantry, name = 'add_ingredient'),
    path('recipe/<int:recipe_id>/', recipe.as_view(), name =
    'view_recipe'),
    path('recipe/', recipe.as_view(), name = 'make_recipe'),
    path('recipe/<str:search_terms>/', search, name = 'search'),
]