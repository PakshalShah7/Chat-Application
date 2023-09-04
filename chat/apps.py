"""This file is created to help us to include any application configuration for the app."""

from django.apps import AppConfig


class ChatConfig(AppConfig):
    """
    This class represents a Django application and its configurations.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'
