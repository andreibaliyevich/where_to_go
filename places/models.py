from django.db import models
from .utilities import get_image_path


class Place(models.Model):
    """ Place Model """
    title = models.CharField(max_length=128, verbose_name='Название')

    description_short = models.CharField(
        max_length=256,
        verbose_name='Короткое описание',
    )
    description_long = models.TextField(verbose_name='Описание (полное)')

    coordinates_lng = models.FloatField(verbose_name='Координаты (долгота)')
    coordinates_lat = models.FloatField(verbose_name='Координаты (широта)')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['-id']


class Image(models.Model):
    """ Image Model """
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место',
    )
    image = models.ImageField(
        upload_to=get_image_path,
        verbose_name='Изображение',
    )
    order = models.IntegerField(default=0, verbose_name='Очередь')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['place', 'order']
