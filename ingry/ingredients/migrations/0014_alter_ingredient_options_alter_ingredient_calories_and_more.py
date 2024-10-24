# Generated by Django 5.1.1 on 2024-10-17 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0013_ingredient_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name'], 'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='calories',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Калории'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='carbohydrates',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Углеводы'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='category',
            field=models.CharField(choices=[('Ов', 'Овощь'), ('Фр', 'Фрукт'), ('Зр', 'Зерно'), ('Мл', 'Молочный продукт'), ('Сп', 'Специя'), ('Др', 'Другое')], verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='fats',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Жиры'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='fiber',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Клетчатка'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='image',
            field=models.ImageField(default='', upload_to='ingredients', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='minerals',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Минералы'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='proteins',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Протеины'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='sodium',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Натрий'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='sugars',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Сахара'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='vitamins',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Витамины'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='Вес'),
        ),
    ]
