from django.contrib import admin
from .models import Category, SubCategory, Product


# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('name', 'is_published')
    list_filter = ('is_published',)
    #actions = (make_published, make_unpublished)
    # search_fields = ('parent', 'id')
    search_help_text = 'Введите имя родительской категории или id категории'
    #inlines = (ProductTabularInline,)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('name', 'is_published')
    list_filter = ('is_published',)
    #actions = (make_published, make_unpublished)
    # search_fields = ('parent', 'id')
    search_help_text = 'Введите имя родительской категории или id категории'
    #inlines = (ProductTabularInline,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('title', 'article', 'category', 'price', 'is_published')
    list_filter = ('is_published', 'category', 'count')
    search_fields = ('title', 'id', 'article', 'price')
    # actions = (make_published, make_unpublished)
    search_help_text = 'Введите имя товара, id , артикул, цену'
    fieldsets = (
        ('Основные настройки',
         {
             'fields': ('title', 'article', 'price', 'category', 'sub_category'),
             # 'description': 'описание'
         }
         ),
        ('Дополнительные настройки',
         {'fields': ('is_published', 'descr', 'count',
                     # 'characteristics'
                     )

          }
         )
    )
    list_editable = ('category',)
    prepopulated_fields = {'descr': ('title', 'article')}
