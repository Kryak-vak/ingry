from django.shortcuts import render, redirect

from .forms import AddIngredientForm
from .models import Ingredient


def index(request):
    context = {
        'title': 'Ингредиенты',
        'active_menu_url_name': request.resolver_match.url_name, 
        'ingridients': Ingredient.objects.all()
    }

    return render(request, 'ingredients/ingredients.html', context)


def show_ingredient(request, ingredient_slug):
    ingredient = Ingredient.objects.get(slug=ingredient_slug)

    context = {
        'title': ingredient.name,
        'active_menu_url_name': request.resolver_match.url_name, 
        'ingredient': ingredient
    }

    return render(request, 'ingredients/ingredient.html', context)


def add_ingredient(request):
    print(f'{request.method = }')
    if request.method == 'POST':
        form = AddIngredientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            redirect('add_ingredient')
    else:
        form = AddIngredientForm()
    
    context = {
        'title': 'Добавление ингредиента',
        'active_menu_url_name': request.resolver_match.url_name,
        'form': form
    }

    return render(request, 'ingredients/add_ingredient.html', context)

