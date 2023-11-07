from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from booking.models import Booking, StatusBooking
from django.db.models import F, ExpressionWrapper, DecimalField


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    #  поля на странице списка объектов.
    list_display = ['id', 'status', 'number_booking', 'date_in', 'date_out',
                    'room', 'room_number', 'count_adult',
                    'surname', 'name', 'patronymic', 'phone', 'email', 'comment', 'ds', 'du',
                    'calculated_days', 'room_link', 'roomnumber_link', 'price', 'cost'
                    ]

    # порядок полей в окне просмотра объекта
    fields = ('status', 'number_booking', 'date_in', 'date_out',
              'room', 'room_number', 'count_adult',
              'surname', 'name', 'patronymic', 'phone', 'email', 'comment', 'ds', 'du',
              'calculated_days', 'room_link', 'roomnumber_link', 'price', 'cost')

    # поля, которые можно редактировать на странице списка объектов
    list_editable = ['status', ]

    # # Поля для поиска
    # search_fields = ('room__startswith',)

    # Фильтры
    list_filter = ('date_in', 'date_out')

    # Поля только для чтения
    readonly_fields = ('number_booking', 'date_in', 'date_out', 'room', 'room_number',
                       'count_adult',
                       # 'surname', 'name', 'patronymic',
                       'phone', 'email', 'comment',
                       'ds', 'du',
                       'calculated_days', 'room_link', 'roomnumber_link', 'price', 'cost')

    # -----------------------вычисляемое поле-------------------------------------
    # https://stackoverflow.com/questions/42659741/django-admin-enable-sorting-for-calculated-fields
    def calculated_days(self, obj):
        return (obj.date_out - obj.date_in).days

    calculated_days.short_description = 'Количество дней'

    # ----------------------ссылка на номер--------------------------------------
    def room_link(self, obj):
        url = reverse('admin:rooms_room_change', args=[obj.room.id])
        return format_html("<a href='{}'>{}</a>", url, obj.room.name)

    room_link.short_description = 'Тип номера'

    # ---------------------ссылка на комнату------------------------------------
    def roomnumber_link(self, obj):
        url = reverse('admin:rooms_roomnumber_change', args=[obj.room_number.id])
        return format_html("<a href='{}'>{}</a>", url, obj.room_number.number)

    roomnumber_link.short_description = 'Номер комнаты'

    # ----------------------цена за номер-----------------------------------------
    def price(self, obj):
        return obj.room.price

    price.short_description = 'Цена (руб/сутки)'

    # ----------------------стоимость за проживание--------------------------------
    def cost(self, obj):
        return obj.room.price * self.calculated_days(obj)

    cost.short_description = 'Стоимость (руб)'


@admin.register(StatusBooking)
class StatusBookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ds', 'du']
