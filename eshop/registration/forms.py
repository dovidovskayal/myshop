from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput, CharField, EmailField


class SingUpForm(UserCreationForm):
    username = CharField(
        widget=TextInput(
            attrs={
                'type': 'username',
                'id': 'register_username',
                'placeholder': 'Your Username'
            }
        )
    )
    password1 = CharField(
        widget=PasswordInput(
            attrs={
                'name': 'pass',
                'id': 'pass',
                'placeholder': 'Enter Your Password'
            }
        )
    )
    password2 = CharField(
        widget=PasswordInput(
            attrs={
                'name': 're_pass',
                'id': 're_pass',
                'placeholder': 'Repeat Your Password'
            }
        )
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'type': 'username',
                'id': 'register_username',
                'placeholder': 'Enter Your Email'
            }
        )
    )


class SignInForm(AuthenticationForm):
    username = UsernameField(
        widget=TextInput(
            attrs={
                'name': 'your_name',
                'id': 'your_name',
                'placeholder': 'Enter Your Username'
            }
        )
    )
    password = CharField(
        widget=PasswordInput(
            attrs={
                'name': 'your_pass',
                'id': 'your_pass',
                'placeholder': 'Enter Your Password'
            }
        )
    )