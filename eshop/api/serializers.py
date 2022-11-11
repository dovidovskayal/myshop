from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from shop.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = ('name', 'descr', 'is_published',)

