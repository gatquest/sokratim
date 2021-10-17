from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Favorite(models.Model):
    link_name = models.CharField('Длинная ссылка',max_length=300) # для создания ссылки
    short_name =models.CharField('Сокращенная ссылка', max_length=50, unique=True) # для создания названия?
    avtor = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE,)

    def __str__(self):
        return self.short_name

    def get_absolute_url(self):
        return reverse('favorites')


# Create your models here.
