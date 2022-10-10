from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import Category, Product
from django.shortcuts import render, get_object_or_404


def index(request: HttpRequest):
    categories = Category.objects.all().order_by('name')
    products = Product.objects.filter(is_published=1).order_by('title')
    return render(request, 'app/index.html', {'categories': categories, 'products': products}, status=200)


def error404(request, exception):
    return HttpResponse('<b>404</b>')
