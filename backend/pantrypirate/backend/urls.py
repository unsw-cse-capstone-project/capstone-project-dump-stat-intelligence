from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.authtoken import views
from django.contrib.auth import views as auth

# Router recognises url patterns and request types, sending them to the
# appropriate views
router = routers.DefaultRouter()
router.register(r'user/pantry', PantryIngredientViewSet, basename='pantry')
router.register(r'user', UserViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'user/cookbook', CookbookViewSet, basename='cookbook')
router.register(r'user/myrecipes', MyRecipesViewSet)

urlpatterns = [

    # User Related Paths - put in first to take priority over the user viewset
    path('user/login/', CustomObtainAuthToken.as_view()),
    path('user/register/', UserCreate.as_view()),
    path('user/logout/', UserLogout.as_view()),

    # Auto routes and API routes
    path('', include(router.urls)),
    path('api-token-auth/', include(
        'rest_framework.urls'), name='api-tokn-auth'),
]
