from django.db import models


class Place(models.Model):
    """ Place Model """
    title = models.CharField(max_length=128, verbose_name='Название')

    description_short = models.CharField(
        max_length=200,
        verbose_name='Короткое описание',
    )
    description_long = models.TextField(verbose_name='Описание (полное)')

    coordinates_lng = models.FloatField(verbose_name='Координаты (долгота)')
    coordinates_lat = models.FloatField(verbose_name='Координаты (широта)')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['-id']
