# Generated by Django 3.2.22 on 2023-11-02 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0009_alter_statusfeedback_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='FIO',
            field=models.CharField(max_length=100, verbose_name='ФИО'),
        ),
    ]
