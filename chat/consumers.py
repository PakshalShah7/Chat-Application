"""This file contains consumer for chat application"""

import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User

from chat.models import Room, Chat


class ChatConsumer(AsyncWebsocketConsumer):
    """
    This class contains chat consumer.
    """
    @sync_to_async
    def create_new_message(self, me, message, room_name):
        """
        This method will store and create new messages in a chat model.
        """
        return Chat.objects.create(room=room_name, from_user=me, text=message)

    async def connect(self):
        """
        This method is used to join a room group.
        """
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join a room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        """
        This method is used to leave a room group.
        """
        # Leave a room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        """
        This method will receive a message from websocket and send it to a room group
        """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        from_user = User.objects.get(username=username)
        room_id = Room.objects.get(name=self.room_name)

        await self.create_new_message(me=from_user, message=message, room_name=room_id)

        # Send a message to a room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": username
            }
        )

    # Receive a message from a room group
    async def chat_message(self, event):
        """
        This method will receive a message from a room group and send it to websocket.
        """
        message = event['message']
        username = event['username']

        # Send a message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
