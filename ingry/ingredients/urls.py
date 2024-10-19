from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ingredients'),
    path('ingredients/<slug:ingredient_slug>/', views.show_ingredient, name='ingredient'),
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),
]
