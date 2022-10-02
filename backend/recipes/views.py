from rest_framework.viewsets import ReadOnlyModelViewSet

from .serailizers import IngredientSerializer
from .models import Ingredient


class IngredientViewSet(ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
