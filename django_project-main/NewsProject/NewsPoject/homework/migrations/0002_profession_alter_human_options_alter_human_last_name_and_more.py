# Generated by Django 4.2 on 2023-05-04 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Профессия')),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
                'ordering': ['title'],
            },
        ),
        migrations.AlterModelOptions(
            name='human',
            options={'ordering': ['id'], 'verbose_name': 'людей', 'verbose_name_plural': 'Люди'},
        ),
        migrations.AlterField(
            model_name='human',
            name='Last_name',
            field=models.TextField(blank=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='human',
            name='Name',
            field=models.CharField(max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='human',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='human',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='human',
            name='photo',
            field=models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='human',
            name='profession',
            field=models.CharField(max_length=150, verbose_name='Профессия'),
        ),
        migrations.AddField(
            model_name='human',
            name='profess',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='homework.profession', verbose_name='Професс'),
        ),
    ]
