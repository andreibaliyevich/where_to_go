from tinymce.models import HTMLField
from django.db import models
from .utilities import get_image_path


class Place(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')

    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = HTMLField(verbose_name='Описание (полное)')

    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['-id']


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место',
    )
    image = models.ImageField(
        upload_to=get_image_path,
        verbose_name='Изображение',
    )
    position = models.PositiveIntegerField(
        default=0,
        db_index=True,
        verbose_name='Позиция',
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['position']
