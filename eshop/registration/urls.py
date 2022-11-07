from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import SingUpView, SignInView, ProfileView

urlpatterns = [
    path('', SignInView.as_view(), name='login'),
    path('register/', SingUpView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='account'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    ]