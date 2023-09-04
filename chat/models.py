"""This file contains room and chat models."""

from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Room(TimeStampedModel):
    """
    This model will store room details.
    """
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(User)

    def __str__(self):
        """
        The method allows us to convert an object into a string representation.
        """
        return self.name


class Chat(TimeStampedModel):
    """
    This model will store chat details.
    """
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='rooms')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_msg')
    text = models.CharField(max_length=300)

    def __str__(self):
        """
        The method allows us to convert an object into a string representation.
        """
        return self.room.name
