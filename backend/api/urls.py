from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.users import UsersViewSet
from api.views.recipes import IngredientViewSet, RecipeViewSet, TagViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'tags', TagViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
