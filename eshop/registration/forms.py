from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput


class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': TextInput(
                attrs={
                    'email': 'register_username',
                    # 'id': 'name',
                    # 'placeholder': 'Your Username'
                }
            ),
            'password': PasswordInput(
                attrs={
                    'password': 'register_pwsd',
                    # 'id': 'pass',
                    # 'placeholder': 'Enter Your Password'
                }
            )
        }