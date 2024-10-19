from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)


class Items(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()

