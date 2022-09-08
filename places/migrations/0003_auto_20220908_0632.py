# Generated by Django 3.2 on 2022-09-08 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['place', 'order'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AddField(
            model_name='image',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Очередь'),
        ),
    ]