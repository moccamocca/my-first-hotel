from django import forms
from phonenumber_field.formfields import PhoneNumberField

from feedback.models import Feedback, StatusFeedback


class FeedbackForm(forms.ModelForm):
    personal_data = forms.BooleanField(label="Я согласен на обработку персональных данных",
                                       required=True)
    phone = PhoneNumberField(region="RU",
                             widget=forms.TextInput(attrs={'placeholder': 'Телефон'}),
                             required=True,
                             label='')

    # поле выбора из всех статусов
    status = forms.ModelChoiceField(
        queryset=StatusFeedback.objects.all(),
        widget=forms.HiddenInput  # скрыть
    )

    class Meta:
        model = Feedback
        fields = ['FIO', 'phone', 'email', 'message', 'status']

        widgets = {
            'FIO': forms.TextInput(attrs={'placeholder': 'ФИО'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email адрес'}),
            'message': forms.Textarea(attrs={'placeholder': 'Сообщение'}),
        }

        labels = {
            'FIO': '',
            'phone': '',
            'email': '',
            'message': '',
        }
