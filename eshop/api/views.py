from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from api.serializers import CategorySerializer, ProductSerializer
from shop.models import Category, Product


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_published=True)
    serializer_class = ProductSerializer

