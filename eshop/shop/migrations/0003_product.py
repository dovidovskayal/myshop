# Generated by Django 4.1.1 on 2022-10-01 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Макс. 24 символа', max_length=24, null=True, verbose_name='название товара')),
                ('price', models.DecimalField(decimal_places=2, default=0, help_text='Макс. 999999.99', max_digits=8, verbose_name='цена')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='количество')),
                ('article', models.CharField(help_text='Макс. 16 символов', max_length=16, unique=True, verbose_name='артикул')),
                ('descr', models.CharField(blank=True, help_text='Макс. 140 символов', max_length=140, null=True, verbose_name='описание')),
                ('is_published', models.BooleanField(default=False, verbose_name='публикация')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category', verbose_name='категория')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.subcategory', verbose_name='подкатегория')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'db_table': 'shop_products',
                'ordering': ('price', 'title', 'article'),
            },
        ),
    ]
