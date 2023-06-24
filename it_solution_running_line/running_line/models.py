from django.db import models
from django.core.validators import MaxValueValidator


class TextData(models.Model):
    text = models.CharField(verbose_name='Введите текст:', max_length=200)
    duration = models.IntegerField(verbose_name='Введите длительность видео:', validators=[MaxValueValidator(100)],
                                   default=3)
    weight = models.IntegerField(verbose_name='Введите длину видео:', validators=[MaxValueValidator(1980)],
                                 default=112)
    height = models.IntegerField(verbose_name='Введите ширину видео:', validators=[MaxValueValidator(1980)],
                                 default=112)
    size_text = models.IntegerField(verbose_name='Введите размер текста:', validators=[MaxValueValidator(500)],
                                 default=40)
