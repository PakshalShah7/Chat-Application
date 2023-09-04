"""This file is used to display models in the Django admin panel."""

from django.contrib import admin
from django.contrib.auth.models import Group

from chat.models import Room, Chat

admin.site.unregister(Group)
admin.site.site_header = "Chat Application"


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """
    This class will register a room model in admin site.
    """
    date_hierarchy = 'created'
    search_fields = ['name__icontains', 'users__username__icontains']
    list_display = ['name']
    list_per_page = 10


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    """
    This class will register a chat model in admin site.
    """
    date_hierarchy = 'created'
    search_fields = ['room__name__icontains', 'from_user__icontains']
    list_display = ['room', 'from_user', 'text']
    list_per_page = 10
