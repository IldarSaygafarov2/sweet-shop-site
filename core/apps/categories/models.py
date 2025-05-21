from django.db import models
from django.urls import reverse
from core.apps.base_app.models import BaseModel


class Category(BaseModel):
    name = models.CharField(verbose_name='Название', max_length=150, unique=True)
    slug = models.SlugField(verbose_name='Короткая ссылка', help_text='Данное поле заполнять не нужно', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(BaseModel):
    name = models.CharField(verbose_name='Название', max_length=150, unique=True)
    slug = models.SlugField(verbose_name='Короткая ссылка', unique=True, help_text='Данное поле заполнять не нужно')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories',
                                 verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

