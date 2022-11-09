from django.urls import path, register_converter, re_path

from .views import index, about, product, ProductDetailsView
from django.conf.urls import handler404


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('product/<slug:product_slug>/', ProductDetailsView.as_view(), name='product_details'),

]

handler404 = 'shop.views.error404'
