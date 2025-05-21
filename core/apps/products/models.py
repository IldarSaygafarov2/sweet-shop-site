from django.db import models
from django.urls import reverse

from core.apps.base_app.models import BaseModel


class Product(BaseModel):
    name = models.CharField(verbose_name='Название', max_length=150)
    slug = models.SlugField(verbose_name='Короткая ссылка', help_text='Данное поле заполнять не нужно', unique=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    preview_image = models.ImageField(verbose_name='Заставка', upload_to='products/previews/', null=True, blank=True)
    price = models.IntegerField(verbose_name='Цена')
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='categories',
                                 verbose_name='Категория', null=True, blank=True)
    subcategories = models.ManyToManyField('categories.Subcategory', related_name='subcategories',
                                           verbose_name='Подкатегории', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={'product_id': self.pk})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
