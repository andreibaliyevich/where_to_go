# Generated by Django 3.2 on 2022-09-08 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20220908_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.CharField(max_length=256, verbose_name='Короткое описание'),
        ),
    ]
