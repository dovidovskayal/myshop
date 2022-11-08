from django.http import HttpRequest
from django.shortcuts import render
from .forms import ContactForm



def contact(request: HttpRequest):
    error = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Ошибка'
    form = ContactForm()
    return render(request,
                  'contact.html',
                  {
                      'contact_form': form,
                      'contact_error': error
                  })

