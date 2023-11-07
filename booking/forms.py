from django import forms
from django.forms.widgets import SelectDateWidget, DateInput
from datetime import datetime, date, timedelta

from phonenumber_field.formfields import PhoneNumberField

from booking.models import Booking


# фильры для поиска номера
class BookingFilterForm(forms.Form):
    date_min = date.today()
    date_max = date.today() + timedelta(weeks=52)

    date_in = forms.DateField(label='Дата заезда',
                              required=True,
                              widget=DateInput(
                                  attrs={'type': 'date',
                                         'min': date_min,
                                         'max': date_max,
                                         }),
                              )

    date_out = forms.DateField(label='Дата выезда',
                               required=True,
                               widget=DateInput(
                                   attrs={'type': 'date',
                                          'min': date_min,
                                          'max': date_max,
                                          }),
                               )

    CHOICES = (('1', '1 взрослый'),
               ('2', '2 взрослых'),
               ('3', '3 взрослых'),
               ('4', '4 взрослых'),
               ('5', '5 взрослый'),)
    count_adult = forms.ChoiceField(label='Размещение', choices=CHOICES)

    # https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html
    # https://docs.djangoproject.com/en/1.11/ref/models/instances/#django.db.models.Model.clean
    def clean(self):
        cleaned_data = super(BookingFilterForm, self).clean()
        date_in = cleaned_data.get('date_in')
        date_out = cleaned_data.get('date_out')
        count_adult = cleaned_data.get('count_adult')

        if not date_in and not date_out:
            raise forms.ValidationError('Укажите даты!')
        if not count_adult:
            raise forms.ValidationError('Выберите количество гостей!')
        if date_in >= date_out:
            self.add_error('date_out', 'Укажите корректные даты')
            raise forms.ValidationError(
                'Дата выезда должна быть позже , чем дата заезда!')  # используется для ошибок, привязанных ко всей форме, а не к конкретному полю


# форма бронирования
class BookingForm(forms.ModelForm):
    personal_data = forms.BooleanField(label='Я согласен на обратку персональных данных',
                                       required=True)

    phone = PhoneNumberField(region="RU",
                             widget=forms.TextInput(attrs={'placeholder': 'Телефон'}),
                             required=True,
                             label='')

    # неизменяемые поля формы
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_in'].disabled = True
        self.fields['date_out'].disabled = True
        self.fields['count_adult'].disabled = True
        self.fields['room'].disabled = True
        self.fields['room_number'].disabled = True
        self.fields['number_booking'].disabled = True

    class Meta:
        model = Booking
        fields = ['number_booking', 'date_in', 'date_out', 'room', 'room_number', 'count_adult', 'surname', 'name',
                  'patronymic', 'phone',
                  'email', 'comment', ]

        # скрыть поля формы
        widgets = {'date_in': forms.HiddenInput(),
                   'date_out': forms.HiddenInput(),
                   'count_adult': forms.HiddenInput(),
                   'room': forms.HiddenInput(),
                   'number_booking': forms.HiddenInput(),
                   'room_number': forms.HiddenInput(),

                   'surname': forms.TextInput(attrs={'placeholder': 'Фамилия'}),
                   'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
                   'patronymic': forms.TextInput(attrs={'placeholder': 'Отчество'}),
                   'email': forms.TextInput(attrs={'placeholder': 'Электронная почта'}),
                   'comment': forms.Textarea(attrs={'placeholder': 'Комментарий'}),
                   }

        labels = {
            'surname': '',
            'name': '',
            'patronymic': '',
            'phone': '',
            'email': '',
            'comment': '',
        }

    # def clean(self):
    #     cleaned_data = super(BookingForm, self).clean()
    #     phone = cleaned_data.get('phone')
    #
    #     if not phone :
    #         raise forms.ValidationError('Укажите даты!')
