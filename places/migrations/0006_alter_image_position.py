# Generated by Django 4.1.1 on 2022-09-09 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20220908_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(default=0, verbose_name='Позиция'),
        ),
    ]
