from django.core.exceptions import ValidationError
from django.shortcuts import render, HttpResponse
from booking.forms import BookingFilterForm
from rooms.models import Room, RoomOptions, RoomPhoto, RoomNumber
from booking.models import Booking
from django.db.models import Q, Count
from django.contrib import messages
from hotel.function import NotIn
from datetime import datetime


def booking_filter(request):
    form = BookingFilterForm(request.GET)  # GET параметр нужен чтобы форма не очищалась при каждом поиске
    rooms = {}
    options = {}
    photos = {}
    count_night = 0

    if form.is_valid():
        rooms = Room.objects.all()
        options = RoomOptions.objects.all().select_related('option')
        photos = RoomPhoto.objects.all()

        # дата заезда
        if form.cleaned_data['date_in'] and form.cleaned_data['date_out']:
            # 1.1 забронированные номера в даты
            count_night = (form.cleaned_data['date_out'] - form.cleaned_data['date_in']).days

            bookings = Booking.objects.filter(
                Q(date_in__range=(form.cleaned_data['date_in'], form.cleaned_data['date_out'])) |
                Q(date_out__range=(form.cleaned_data['date_in'], form.cleaned_data['date_out'])) |
                Q(Q(date_in__lte=form.cleaned_data['date_in']) &
                  Q(date_out__gte=form.cleaned_data['date_out']))).values_list('room_number', flat=True)

            # 2 отсечь забронированные номера, оставить только свободные
            if bookings:
                rooms = rooms.filter(roomnumber__id__notin=list(bookings))
            else:
                rooms = rooms.filter(roomnumber__id__isnull=False)  # отсечь типы номеров у которых нет комнат

            # 3 учесть вместимость -> нашли свободные комнаты
            if form.cleaned_data['count_adult']:  # поле с формы
                rooms = rooms.filter(capacity__gte=form.cleaned_data['count_adult'])  # capacity - поле модели Room

            # 4 сгруппировать по типам номеров чтобы найти количесвто свободных комнат

            rooms = rooms.values('id', 'name', 'price', 'capacity').annotate(count_room=Count('id')).order_by(
                'id')

            # # 4 вывести только типы номеров - убрать дубли (например у студии может быть нескольок номеров) (в django нет distinct по полям для MSSQL)
            # rooms = rooms.values('id', 'name', 'price', 'capacity').distinct()

            # print(str(bookings.query))
            # print(str(rooms.query))

    return render(request,
                  'booking_filter.html',
                  {'form': form,
                   'rooms': rooms,
                   'options': options,
                   'photos': photos,
                   'date_in': request.GET.get('date_in'),  # ?date_in=2023-10-25&date_out=2023-10-31&count_adult=1
                   'date_out': request.GET.get('date_out'),
                   'count_adult': request.GET.get('count_adult'),
                   'count_night': count_night, }
                  )
