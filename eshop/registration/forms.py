from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput, CharField


class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': TextInput(
                attrs={
                    'type': 'username',
                    'id': 'register_username',
                    # 'placeholder': 'Your Username'
                }
            ),
            'email': TextInput(
                attrs={
                    'type': 'email',
                    'id': 'register_username',
                    # 'placeholder': 'Your Username'
                }
            ),
            'password': PasswordInput(
                attrs={
                    'type': 'password',
                    'id': 'register_pwsd',
                    # 'placeholder': 'Enter Your Password'
                }
            )
        }


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