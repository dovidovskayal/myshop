from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from shop.models import Category, Product



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('article',)


