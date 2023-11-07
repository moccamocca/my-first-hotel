from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class StatusBooking(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=50, null=False, unique=True)
    ds = models.DateTimeField('Дата создания', auto_now_add=True)
    du = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['-ds', ]


class Booking(models.Model):
    date_in = models.DateField(verbose_name='дата заезда', null=False)
    date_out = models.DateField(verbose_name='дата отъезда', null=False)
    count_adult = models.IntegerField(verbose_name='Гости', null=False)
    comment = models.TextField(verbose_name='Комментарий', max_length=5000, default='', blank=True)
    surname = models.CharField(verbose_name='Фамилия', max_length=100, null=False)
    name = models.CharField(verbose_name='Имя', max_length=100, null=False)
    patronymic = models.CharField(verbose_name='Отчество', max_length=100, default='',
                                  blank=True)
    # phone = models.CharField(verbose_name='Телефон', max_length=20, null=False)
    phone = PhoneNumberField(null=False, blank=False)
    email = models.EmailField(verbose_name='email', null=False)
    room = models.ForeignKey('rooms.Room', on_delete=models.PROTECT, null=False, verbose_name='Тип номера')
    room_number = models.ForeignKey('rooms.RoomNumber',
                                    on_delete=models.PROTECT,
                                    verbose_name='Номер комнаты')
    status = models.ForeignKey('StatusBooking',
                               on_delete=models.PROTECT,
                               verbose_name='Статус',
                               default=StatusBooking.objects.get(pk=1).id)
    number_booking = models.CharField('Номер бронирования', max_length=50, unique=True, null=False)

    ds = models.DateTimeField('Дата создания', auto_now_add=True)
    du = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'
        ordering = ['-ds', 'date_in', 'date_out', 'room', 'room_number']
