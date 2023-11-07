from django.contrib import admin
from feedback.models import Feedback, StatusFeedback


@admin.register(StatusFeedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'ds']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'FIO', 'phone', 'email', 'ds', 'du', 'message']

    # Поля только для чтения
    readonly_fields = ('id', 'FIO', 'phone', 'email', 'ds', 'du', 'message')

    # поля, которые можно редактировать на странице списка объектов
    list_editable = ['status', ]

    # Фильтры
    list_filter = ('status', )
