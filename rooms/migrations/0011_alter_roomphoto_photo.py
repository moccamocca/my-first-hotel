# Generated by Django 3.2.22 on 2023-11-02 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_auto_20231029_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomphoto',
            name='photo',
            field=models.ImageField(upload_to='hotel/photos', verbose_name='фото'),
        ),
    ]
