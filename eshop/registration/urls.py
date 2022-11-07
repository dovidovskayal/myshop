from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import SingUpView

urlpatterns = [
    path('', SingUpView.as_view(), name='login'),
    # path('signin/', SignInView.as_view(), name='signin'),
    # path('logout/', LogoutView.as_view(), name='logout'),

    ]