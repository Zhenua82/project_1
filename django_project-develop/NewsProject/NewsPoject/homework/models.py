from django.db import models


class Human(models.Model):
    Name = models.CharField(max_length=150, verbose_name='Имя')
    Last_name = models.TextField(blank=True, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    profession = models.CharField(max_length=150, verbose_name='Профессия')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    class Meta:
        verbose_name='людей'
        verbose_name_plural='Люди'
        ordering = ['id']

