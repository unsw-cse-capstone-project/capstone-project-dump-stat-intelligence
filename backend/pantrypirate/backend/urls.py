from django.urls import path
from . import views

urlpatterns = [
    #path('', views.login, name='login'),
    path('user/<int:user_id>/', views.user, name = 'user'),
    #path('/user/{user_id}/cookbook', views.cookbook, name = 'cookbook'),
    path('ingredients/<str:ingredient_name>/', views.ingredients, name =
    'get_ingredient'),
    path('ingredients/', views.ingredients, name = 'set_get_ingredients'),
    path('user/<int:user_id>/pantry/', views.pantry, name = 'pantry'),
    path('user/<int:user_id>/pantry/<int:ingredient_id>', views.pantry, name =
    'delete_ingredient'),
    #path('/user/{user_id}/pantry/{ingredientId}', views.pantry, name = 'add_ingredient'),
    path('recipe/<int:recipe_id>/', views.recipe, name = 'view_recipe'),
    path('recipe/', views.recipe, name = 'make_recipe'),
    path('recipe/<str:search_terms>/', views.search, name = 'search'),
]