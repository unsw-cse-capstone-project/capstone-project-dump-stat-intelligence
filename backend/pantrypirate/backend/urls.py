from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.authtoken import views
from django.contrib.auth import views as auth

router = routers.DefaultRouter()
router.register(r'user/pantry', PantryIngredientViewSet, basename='pantry')
router.register(r'user', UserViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)

urlpatterns = [

    # User Related Paths
    path('user/login/', UserLogin.as_view()),
    path('user/register/', UserCreate.as_view()),
    path('user/logout/', UserLogout.as_view()),

    # Auto routes and API routes
    path('', include(router.urls)),
    path('api-token-auth/', include(
        'rest_framework.urls'), name='api-tokn-auth'),
]
