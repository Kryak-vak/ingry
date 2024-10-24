# Generated by Django 5.0.6 on 2024-07-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0006_alter_ingredient_calories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='calories',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='carbohydrates',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='fats',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='fiber',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='minerals',
            field=models.JSONField(blank=True, default={}, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='proteins',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='sodium',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='sugars',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='vitamins',
            field=models.JSONField(blank=True, default={}, null=True),
        ),
    ]
