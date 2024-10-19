from django.contrib.auth.models import Group, User
from rest_framework import serializers

from items.models import Items


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['category', 'name', 'price']