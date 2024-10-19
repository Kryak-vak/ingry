from django.contrib import admin
from .models import Ingredient

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    ordering = ['name', 'id']
    list_display = ('name', 'id', 'category')
    list_display_links = ('name', 'id')
    list_editable = ('category', )

