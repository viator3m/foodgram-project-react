from django_filters import filters
from django_filters.rest_framework import FilterSet

from recipes.models import Ingredient


class IngredientFilter(FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='istartswith')

    class Meta:
        model = Ingredient
        fields = ('name',)