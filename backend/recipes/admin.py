from django.contrib.admin import ModelAdmin, register

from recipes.models import (Favorite, Ingredient, Recipe, RecipeIngredient,
                            ShoppingCart, Tag)


@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('name', 'color', 'slug')


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = ('name', 'author', 'pub_date', 'display_tags', 'favorite')
    list_filter = ('name', 'author', 'tags')
    search_fields = ('name',)
    readonly_fields = ('favorite',)
    fields = ('image',
              ('name', 'author'),
              'text',
              ('tags', 'cooking_time'),
              'favorite')

    def display_tags(self, obj):
        return ', '.join([tag.name for tag in obj.tags.all()])
    display_tags.short_description = 'Теги'

    def favorite(self, obj):
        return obj.favorite.count()
    favorite.short_description = 'Раз в избранном'


@register(RecipeIngredient)
class RecipeIngredientAdmin(ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')


@register(Favorite)
class FavoriteAdmin(ModelAdmin):
    list_display = ('recipe', 'user')


@register(ShoppingCart)
class ShoppingCartAdmin(ModelAdmin):
    list_display = ('recipe', 'user')
