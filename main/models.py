from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length = 100)
    created = models.DateField(auto_now_add = True)
    is_closed = models.BooleanField(default = False)
    is_favorite = models.BooleanField(default = False)

class BookShop(models.Model):
    title = models.CharField(max_length = 100, verbose_name = 'Заголовок')
    subtitle = models.CharField(max_length=50, verbose_name = 'Подзаголовок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    genre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    year = models.DateTimeField(auto_now_add=False, verbose_name='Год выхоа книги')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')