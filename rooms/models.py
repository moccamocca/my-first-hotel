from django.db import models


class Room(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100, unique=True)
    price = models.IntegerField(verbose_name='Цена')
    capacity = models.IntegerField(verbose_name='Вместимость', default=2)
    ds = models.DateTimeField('Дата создания', auto_now_add=True)
    du = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Тип номера'
        verbose_name_plural = 'Типы номеров'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}/{self.capacity} чел.'


class Option(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=100, unique=True)
    descr = models.CharField(verbose_name='Описание', max_length=1000, blank=True)
    ds = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    du = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Опция'
        verbose_name_plural = 'Опции'
        ordering = ['name']

    def __str__(self):
        return self.name


class RoomOptions(models.Model):
    room = models.ForeignKey('Room', on_delete=models.PROTECT, null=False, verbose_name='Номер')
    option = models.ForeignKey('Option', on_delete=models.PROTECT, null=False, verbose_name='Опция')
    ds = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    du = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Тип номера-опция'
        verbose_name_plural = 'Тип номера-опция'
        ordering = ['room', 'option']
        unique_together = ('room', 'option', )


class RoomPhoto(models.Model):
    room = models.ForeignKey('Room', on_delete=models.PROTECT, null=False, verbose_name='Номер')
    photo = models.ImageField(verbose_name='фото',
                              upload_to='hotel/photos',
                              null=False, )
    ds = models.DateTimeField('Дата создания', auto_now_add=True)
    du = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['room', 'photo']


class RoomNumber(models.Model):
    room = models.ForeignKey('Room', on_delete=models.PROTECT, null=False, verbose_name='Тип номера')
    number = models.IntegerField(verbose_name='Номер комнаты', unique=True)
    etag = models.IntegerField(verbose_name='Этаж')
    ds = models.DateTimeField('Дата создания', auto_now_add=True)
    du = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Номера комнат'
        verbose_name_plural = 'Номер комнаты'
        ordering = ['room', 'number']

    def __str__(self):
        return str(self.number) + '/' + str(self.etag) + '/' + str(self.room)
