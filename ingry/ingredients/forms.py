from django import forms

from .models import Ingredient


class AddIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'category', 'image', 'weight', 'calories', 'proteins', 'fats', 'carbohydrates', 'sugars', 'fiber', 'sodium', 'vitamins', 'minerals']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'category': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-sm'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'proteins': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'fats': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'carbohydrates': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'sugars': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'fiber': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'sodium': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'vitamins': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'minerals': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
        }