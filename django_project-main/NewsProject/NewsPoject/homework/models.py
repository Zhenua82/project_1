from django.db import models


class Human(models.Model):
    Name = models.CharField(max_length=150, verbose_name='Имя')
    Last_name = models.TextField(blank=True, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True, verbose_name='Профессия')
    biography = models.TextField(blank=True, verbose_name='Биография')
    class Meta:
        verbose_name='людей'
        verbose_name_plural='Люди'
        ordering = ['id']

class Profession(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Профессия')

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        ordering = ['title']


