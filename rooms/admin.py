from django.contrib import admin
from rooms.models import Room, Option, RoomOptions, RoomPhoto, RoomNumber


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'capacity', 'ds', 'du']


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'descr',  'ds', 'du']


@admin.register(RoomOptions)
class RoomOptionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'option', 'ds', 'du']
    list_display_links = ['room', 'option']


@admin.register(RoomPhoto)
class RoomPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'photo', 'ds', 'du']
    list_display_links = ['room']


@admin.register(RoomNumber)
class RoomNumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'number', 'etag', 'ds', 'du']
    list_display_links = ['room']
