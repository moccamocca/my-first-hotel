from django.db import models


class StatusFeedback(models.Model):
    name = models.CharField(verbose_name='Статус', max_length=50, unique=True)
    ds = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Feedback(models.Model):
    FIO = models.CharField(verbose_name='ФИО', max_length=100)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    email = models.EmailField(verbose_name='email')
    message = models.TextField(verbose_name='Сообщение', max_length=5000)
    ds = models.DateTimeField(verbose_name='Дата отправки', auto_now_add=True)
    du = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    status = models.ForeignKey(StatusFeedback,
                               verbose_name='Статус обращения',
                               on_delete=models.PROTECT,
                               )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-ds']
