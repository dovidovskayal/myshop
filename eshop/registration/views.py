from django.contrib.auth.forms import UsernameField
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.forms import PasswordInput, CharField, TextInput

from .forms import SingUpForm

# Create your views here.



class SingUpView(CreateView):
    form_class = SingUpForm
    template_name = 'registration/register.html'
    # success_url = reverse_lazy('signin')


# class SignInView(LoginView):
#     template_name = 'registration/base.html'
#     username = UsernameField(
#         widget=TextInput(
#             attrs={
#                 'name': 'your name',
#                 'id': 'your_name',
#                 'placeholder': 'Enter yor username'
#
#             }
#
#         )
#     )
#     password = PasswordInput(
#         attrs={
#             'name': 'your_pass',
#             'id': 'your_pass',
#             'placeholder': 'Enter your password'
#         }
#     )

