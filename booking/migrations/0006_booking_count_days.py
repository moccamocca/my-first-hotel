# Generated by Django 3.2.22 on 2023-10-25 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20231025_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='count_days',
            field=models.IntegerField(default=1, verbose_name='Количество суток'),
        ),
    ]
