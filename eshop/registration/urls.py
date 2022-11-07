from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import SingUpView, SignInView

urlpatterns = [
    path('', SignInView.as_view(), name='login'),
    path('register/', SingUpView.as_view(), name='register'),
    # path('signin/', SignInView.as_view(), name='signin'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    ]