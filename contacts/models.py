from django.db import models


class Contact(models.Model):
    otdel = models.CharField(max_length=150, verbose_name='Отдел')
    email = models.EmailField(verbose_name='email')
    telephone = models.CharField(max_length=150, verbose_name='Телефон', blank=True, default='')
    FIO = models.CharField(max_length=200, verbose_name='ФИО', blank=True, default='')
    ds = models.DateTimeField('Дата создания', auto_now_add=True)
    du = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
        ordering = ['otdel']
