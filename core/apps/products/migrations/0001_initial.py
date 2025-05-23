# Generated by Django 5.2 on 2025-05-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Данное поле заполнять не нужно', unique=True, verbose_name='Короткая ссылка')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to='products/previews/', verbose_name='Заставка')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
