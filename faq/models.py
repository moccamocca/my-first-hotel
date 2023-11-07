from django.db import models


class Faq(models.Model):
    question = models.CharField('Вопрос', max_length=500)
    answer = models.TextField('Ответ')
    ds = models.DateTimeField('Дата создания', auto_now_add=True)
    du = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
        ordering = ['ds']
