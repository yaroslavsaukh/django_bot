from django.db import models
from django.urls import reverse


class User(models.Model):
    tg_id = models.IntegerField(verbose_name='Telegram ID')
    name = models.CharField(max_length=50, verbose_name='User name')
    gender = models.CharField(max_length=10, verbose_name='User gender')

    def __str__(self):
        return str(self.tg_id)

    class Meta:
        verbose_name = 'Bot User'
        verbose_name_plural = 'Bot Users'


class Recipe(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    content = models.TextField(blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created_at')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
