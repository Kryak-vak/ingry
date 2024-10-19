from django.db import models
from django.urls import reverse
from .utils import slugify


class Ingredient(models.Model):
    class IngridientTypes(models.TextChoices):
        VEGETABLE = 'Ов', 'Овощь'
        FRUIT = 'Фр', 'Фрукт'
        GRAIN = 'Зр', 'Зерно'
        DAIRY = 'Мл', 'Молочный продукт'
        SPICE = 'Сп', 'Специя'
        OTHER = 'Др', 'Другое'

    name = models.fields.CharField(max_length=255, unique=True, verbose_name='Название')
    slug = models.fields.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    category = models.CharField(choices=IngridientTypes, verbose_name='Категория')
    image = models.ImageField(default='', upload_to='ingredients', verbose_name='Картинка')
    weight = models.IntegerField(default=0, verbose_name='Вес')
    calories = models.fields.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0, verbose_name='Калории')
    proteins = models.fields.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0, verbose_name='Протеины')
    fats = models.fields.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0, verbose_name='Жиры')
    carbohydrates = models.fields.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0, verbose_name='Углеводы')
    sugars = models.fields.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0, verbose_name='Сахара')
    fiber = models.fields.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0, verbose_name='Клетчатка')
    sodium = models.fields.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0, verbose_name='Натрий')
    vitamins = models.JSONField(blank=True, null=True, default=dict, verbose_name='Витамины')
    minerals = models.JSONField(blank=True, null=True, default=dict, verbose_name='Минералы')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Ingredient, self).save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse('ingredient', kwargs={'ingredient_slug': self.slug})

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['name']
