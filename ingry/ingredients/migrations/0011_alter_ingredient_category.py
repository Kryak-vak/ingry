# Generated by Django 5.0.6 on 2024-07-17 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0010_alter_ingredient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='category',
            field=models.CharField(blank=True, choices=[('Ов', 'Овощь'), ('Фр', 'Фрукт'), ('Зр', 'Зерно'), ('Мл', 'Молочный продукт'), ('Сп', 'Специя'), ('Др', 'Другое')]),
        ),
    ]