# Generated by Django 3.2.22 on 2023-10-25 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_booking_count_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='count_days',
        ),
    ]
