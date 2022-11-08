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


class Brand(models.Model):
    name = models.CharField(max_length=24,
                            verbose_name='Бренд',
                            help_text='Макс. 24 символа')
    is_published = models.BooleanField(default=False,
                                       verbose_name='публикация')
    image = models.ImageField(
        upload_to='brands',
        verbose_name='картинка бренда',
        null=True,
        blank=True
    )


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_brands'
        verbose_name = 'бренд'
        verbose_name_plural = 'бренды'
        ordering = ('name', 'is_published')


class Product(models.Model):
    title = models.CharField(max_length=48,
                             verbose_name='название товара',
                             help_text='Макс. 48 символа',
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
                              on_delete=models.CASCADE,
                              verbose_name='бренд',
                              help_text='Макс. 16 символов')
    is_published = models.BooleanField(default=False,
                                       verbose_name='публикация')
    point = models.PositiveSmallIntegerField(default=0,
                                             verbose_name='рейтинг')
    image = models.ImageField(
        upload_to='products',
        verbose_name='картинка продукта',
        null=True,
        blank=True,
        default='images/shop/2.webp'
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'shop_products'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('price', 'title', 'article')


class Comment(models.Model):
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
                                        verbose_name='Дата создания')

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'shop_comments'
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        ordering = ('date_created', 'user', 'product')


class Order(models.Model):
    user = models.ForeignKey(User,
                             verbose_name='пользователь',
                             on_delete=models.DO_NOTHING)
    # order_status = models.OneToOneField('Status',
    #                               verbose_name='статус заказа',
    #                               on_delete=models.DO_NOTHING
    #                               )
    date_created = models.DateTimeField(default=datetime.now,
                                        blank=True,
                                        verbose_name='Дата создания'
                                        )

    def __str__(self):
        return 'Order {}'.format(self.user)

    class Meta:
        db_table = 'shop_orders'
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('date_created', 'user')


class OrderItem(models.Model):
    order = models.ForeignKey('Order',
                              verbose_name='заказ',
                              on_delete=models.DO_NOTHING
                              )
    product = models.ForeignKey('Product',
                                verbose_name='продукты в заказе',
                                on_delete=models.DO_NOTHING
                                )

    class Meta:
        db_table = 'shop_order_items'
        verbose_name = 'содержание заказа'
        verbose_name_plural = 'содержание заказов'
        ordering = ('order', 'product')



class NewsLetter(models.Model):
    email = models.CharField(max_length=48,
                             verbose_name='почта для новостей',
                             help_text='Макс. 48 символов'
                             )

    def __str__(self):
        return self.email


    class Meta:
        db_table = 'shop_news_letters'
        verbose_name = 'подписка на новости'
        verbose_name_plural = 'подписки на новости'
        ordering = ('email',)

# class Status(models.Model):
#     order = models.ForeignKey('Order',
#                               verbose_name='номер заказа',
#                               on_delete=models.CASCADE
#                               )
#     is_paid = models.BooleanField(default=False,
#                                   verbose_name='статус оплаты'
#                                   )
#
#     class Meta:
#         db_table = 'shop_statuses'
#         verbose_name = 'статус заказа'
#         verbose_name_plural = 'статусы заказов'
#         ordering = ('is_paid',)
