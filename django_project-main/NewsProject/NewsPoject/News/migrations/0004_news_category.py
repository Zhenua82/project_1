# Generated by Django 4.2 on 2023-05-03 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='News.category', verbose_name='Категория'),
        ),
    ]
