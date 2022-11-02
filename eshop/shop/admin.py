from django.contrib import admin
from .models import Category, SubCategory, Product, Comment, Brand, Order, OrderItem, NewsLetter


# Register your models here.

class ProductTabularInline(admin.TabularInline):
    model = Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('name', 'is_published')
    list_filter = ('is_published',)
    # actions = (make_published, make_unpublished)
    # search_fields = ('parent', 'id')
    search_help_text = 'Введите имя родительской категории или id категории'
    # inlines = (ProductTabularInline,)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('name', 'is_published')
    list_filter = ('is_published',)
    # actions = (make_published, make_unpublished)
    # search_fields = ('parent', 'id')
    search_help_text = 'Введите имя родительской категории или id категории'
    # inlines = (ProductTabularInline,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('title', 'article', 'category', 'brand', 'price', 'is_published')
    list_filter = ('is_published', 'category', 'count')
    search_fields = ('title', 'id', 'article', 'price')
    # actions = (make_published, make_unpublished)
    search_help_text = 'Введите имя товара, id , артикул, цену'
    fieldsets = (
        ('Основные настройки',
         {
             'fields': ('title', 'article', 'price', 'category', 'sub_category', 'brand',),
             # 'description': 'описание'
         }
         ),
        ('Дополнительные настройки',
         {'fields': ('is_published', 'descr', 'count', 'image',
                     # 'characteristics'
                     )

          }
         )
    )
    list_editable = ('category',)
    prepopulated_fields = {'descr': ('title', 'article')}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('user', 'product', 'date_created')
    list_filter = ('product', 'date_created')
    list_max_show_all = 10


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('name', 'is_published')
    list_filter = ('name', 'is_published')
    list_max_show_all = 10
    inlines = (ProductTabularInline,)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('user', 'date_created')
    list_filter = ('user', 'date_created')
    list_max_show_all = 10


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('order', )
    list_filter = ('order', 'product')
    list_max_show_all = 10



@admin.register(NewsLetter)
class NewsLetter(admin.ModelAdmin):
    list_display = ('email',)
    list_filter = ('email',)



# @admin.register(Status)
# class StatusAdmin(admin.ModelAdmin):
#     empty_value_display = 'N/a'
#     list_display = ('is_paid',)
#     list_filter = ('is_paid', )
#     list_max_show_all = 10