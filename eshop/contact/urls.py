from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import contact

urlpatterns = [
    path('', contact, name='contact'),
    ]