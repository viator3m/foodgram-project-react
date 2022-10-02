from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UsersViewSet
from recipes.views import IngredientViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'ingredients', IngredientViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
