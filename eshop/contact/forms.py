from django.forms import ModelForm, TextInput, EmailInput
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message',)
        widgets = {
            'first_name': TextInput(
                attrs={

                    'class': 'form-control',
                    'type': 'text',
                    'name': 'con_name',
                    'placeholder': 'First Name'

                }
            ),
            'last_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Last Name'
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'name': 'con_email',
                    'placeholder': 'Email Address'
                }
            ),
            'message': TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'con_message',
                    'placeholder': 'Message'

                }
            )
        }