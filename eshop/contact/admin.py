from django.contrib import admin
from .models import Contact

# Register your models here.


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'date_created', 'email',)
    list_filter = ('email', 'date_created')
