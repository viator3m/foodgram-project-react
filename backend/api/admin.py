from django.contrib import admin

from recipes.models import Ingredient, Recipe, Tag
from users.models import User


admin.site.register(User)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Tag)
