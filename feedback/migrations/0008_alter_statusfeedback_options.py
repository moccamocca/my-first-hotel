# Generated by Django 3.2.22 on 2023-10-19 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0007_auto_20231014_2209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statusfeedback',
            options={'ordering': ['name'], 'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
    ]