from django.db import models
from django.core.validators import MaxValueValidator


class TextData(models.Model):
    text = models.CharField(verbose_name='Введите текст, который будет представлен в видео:', max_length=200)
    duration = models.IntegerField(verbose_name='Введите длительность видео (максимум 100 сек.):', validators=[MaxValueValidator(100)],
                                   default=3)
    weight = models.IntegerField(verbose_name='Введите длину видео (максимум 1920 px):', validators=[MaxValueValidator(1920)],
                                 default=100)
    height = models.IntegerField(verbose_name='Введите ширину видео (макисмум 1080 px):', validators=[MaxValueValidator(1080)],
                                 default=100)
    size_text = models.IntegerField(verbose_name='Введите размер текста, который будет представлен в видео (максимум 500):', validators=[MaxValueValidator(500)],
                                 default=40)
