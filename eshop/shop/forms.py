from django.forms import ModelForm, EmailInput, TextInput
from .models import NewsLetter


class NewsLetterForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = ('email',)
        widgets = {
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'enter your email'

                }
            )
        }