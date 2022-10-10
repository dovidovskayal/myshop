from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=24,
                            verbose_name='название категории',
                            help_text='Макс. 24 символа')
    descr = models.CharField(max_length=140,
                             blank=True,
                             null=True,
                             verbose_name='описание',
                             help_text='Макс. 140 символов'
                             )
    is_published = models.BooleanField(default=False,
                                       verbose_name='публикация')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('is_published', 'name')


class SubCategory(models.Model):
    name = models.CharField(max_length=24,
                            verbose_name='название подкатегории',
                            help_text='Макс. 24 символа')
    parent = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='род. категория')
    descr = models.CharField(max_length=140,
                             blank=True,
                             null=True,
                             verbose_name='описание',
                             help_text='Макс. 140 символов'
                             )
    is_published = models.BooleanField(default=False,
                                       verbose_name='публикация')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_sub_categories'
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'
        ordering = ('is_published', 'name')


class Product(models.Model):
    title = models.CharField(max_length=24,
                             verbose_name='название товара',
                             help_text='Макс. 24 символа',
                             null=True,
                             blank=True

                             )
    category = models.ForeignKey('Category',
                                 on_delete=models.PROTECT,
                                 verbose_name='категория')
    sub_category = models.ForeignKey('SubCategory',
                                     on_delete=models.PROTECT,
                                     verbose_name='подкатегория')
    # characteristics = models.ForeignKey('Characteristics',
    #                                     on_delete=models.PROTECT,
    #                                     verbose_name='характеристики',
    #                                     null=True,
    #                                     blank=True
    #
    #
    # )
    price = models.DecimalField(decimal_places=2,
                                max_digits=8,
                                default=0,
                                verbose_name='цена',
                                help_text='Макс. 999999.99',
                                )
    count = models.PositiveSmallIntegerField(default=0,
                                             verbose_name='количество')
    article = models.CharField(max_length=16,
                               verbose_name='артикул',
                               help_text='Макс. 16 символов',
                               unique=True)
    descr = models.CharField(max_length=140,
                             blank=True,
                             null=True,
                             verbose_name='описание',
                             help_text='Макс. 140 символов'
                             )
    brand = models.ForeignKey('Brand',
                              default='нет бренда',
                              verbose_name='бренд',
                              help_text='Макс. 16 символов')
    is_published = models.BooleanField(default=False,
                                       verbose_name='публикация')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'shop_products'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('price', 'title', 'article')


class Comments(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING,
                             verbose_name='пользователь')
    product = models.ForeignKey('Product',
                                on_delete=models.DO_NOTHING,
                                verbose_name='товар')
    comment = models.CharField(max_length=1024,
                               verbose_name='комментарий',
                               help_text='Макс. 1024 символов'
                               )
    date_created = models.DateTimeField(default=datetime.now,
                                        blank=True,
                                        verbose_name='Дата')

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'shop_comments'
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        ordering = ('date_created', 'user', 'product')


class Brand(models.Model):
    name = models.CharField(max_length=24,
                            default='нет бренда',
                            verbose_name='Бренд',
                            help_text='Макс. 24 символа')
    products = models.ForeignKey('Product',
                                 verbose_name='Продукт бренда'
                                 )
