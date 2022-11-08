from django.db import models
from datetime import datetime


# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=48,
                                  verbose_name='Your first name',
                                  help_text='Макс. 48 символов'
                                  )
    last_name = models.CharField(max_length=48,
                                 verbose_name='Your last name',
                                 help_text='Макс. 48 символов'
                                 )
    email = models.CharField(max_length=48,
                             verbose_name='Your email',
                             help_text='Макс. 48 символов'
                             )
    message = models.CharField(max_length=1024, verbose_name='сообщение')
    date_created = models.DateTimeField(default=datetime.utcnow(), verbose_name='дата публикации')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'contacts'
        verbose_name = 'обращение'
        verbose_name_plural = 'обращения'
        ordering = ('email',)
