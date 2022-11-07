from django.contrib.auth.forms import UsernameField, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.forms import PasswordInput, CharField, TextInput, EmailInput

from .forms import SingUpForm

# Create your views here.
from shop.models import Order, OrderItem


class SingUpView(CreateView):
    form_class = SingUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class SignInView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('')
    username = UsernameField(
        widget=TextInput(
            attrs={
                'name': 'your name',
                'id': 'your_name',
                'placeholder': 'Enter yor username'

            }

        )
    )

    password = PasswordInput(
        attrs={
            'name': 'your_pass',
            'id': 'your_pass',
            'placeholder': 'Enter your password'
        }
    )


class ProfileView(LoginRequiredMixin, View):
    template_name = 'profile.html'
    login_url = 'login'


    def get(self, request: HttpRequest) -> HttpResponse:
        user = User.objects.filter(username=request.user)[0]
        return render(request, self.template_name, {'user': user})


    def get_orders(self, request: HttpRequest) -> HttpResponse:
        order = OrderItem.objects.filter(username=request.user)[0]
        return render(request, self.template_name, {'order': order})
