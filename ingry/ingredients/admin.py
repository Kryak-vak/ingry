from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Ingredient

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    ordering = ['name', 'id']
    list_display = ('name', 'ingredient_image', 'id', 'category')
    list_display_links = ('name', 'id')
    list_editable = ('category', )

    @admin.display(description='Картинка')
    def ingredient_image(self, ingredient: Ingredient):
        return mark_safe(f'<img src="{ingredient.image.url}" width=80>')

