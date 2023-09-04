"""This file contains routing for chat consumer websocket."""

from django.urls import re_path

from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r"chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi())
]
