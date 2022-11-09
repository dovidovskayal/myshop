from django.forms import ModelForm, EmailInput, TextInput
from .models import NewsLetter, Comment


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


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'name', 'feedback',)
        widgets = {
            'feedback': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter you feedback'

                }
            ),
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder':'Full Name'

                }
            ),
             'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'type': 'email',
                    'placeholder': 'Email Address'

                })

        }