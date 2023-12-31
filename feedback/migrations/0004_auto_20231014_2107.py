# Generated by Django 3.2.22 on 2023-10-14 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_alter_feedback_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='date_close',
        ),
        migrations.AddField(
            model_name='feedback',
            name='du',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.CharField(blank=True, choices=[('0', 'Создана'), ('1', 'Просмотрена'), ('2', 'Закрыта'), ('3', 'Не получилось связаться')], default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='FIO',
            field=models.CharField(help_text='Введите ФИО', max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(max_length=5000, verbose_name='Сообщение'),
        ),
    ]
