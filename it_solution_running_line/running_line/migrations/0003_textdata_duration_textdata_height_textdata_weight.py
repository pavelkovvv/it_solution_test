# Generated by Django 4.2.2 on 2023-06-24 21:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running_line', '0002_alter_textdata_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='textdata',
            name='duration',
            field=models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Введите длительность видео:'),
        ),
        migrations.AddField(
            model_name='textdata',
            name='height',
            field=models.IntegerField(default=112, validators=[django.core.validators.MaxValueValidator(1980)], verbose_name='Введите ширину символов в видео:'),
        ),
        migrations.AddField(
            model_name='textdata',
            name='weight',
            field=models.IntegerField(default=112, validators=[django.core.validators.MaxValueValidator(1980)], verbose_name='Введите длину символов в видео:'),
        ),
    ]
