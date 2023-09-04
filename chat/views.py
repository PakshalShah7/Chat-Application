"""This file contains class based views for signup and room model."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from chat.forms import RoomForm, SignupForm
from chat.models import Room, Chat


class SignupView(CreateView):
    """
    This class will create a new user instance.
    """
    form_class = SignupForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('chat:login')


class RoomCreateView(LoginRequiredMixin, CreateView):
    """
    This class will create a new room instance.
    """
    form_class = RoomForm
    success_url = reverse_lazy('chat:room_list')


class RoomListView(LoginRequiredMixin, ListView):
    """
    This class will display a list of rooms.
    """
    model = Room
    template_name = 'room/room_list.html'
    context_object_name = 'rooms'

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        This method is used to pass extra context.
        """
        context = super(RoomListView, self).get_context_data(**kwargs)
        context.update({
            'form': RoomForm
        })
        return context

    def get_queryset(self):
        """
        This method will return queryset of a room model.
        """
        return Room.objects.filter(users__in=[self.request.user.id]).order_by('-created')


class RoomDetailView(LoginRequiredMixin, DetailView):
    """
    This class will display a room detail.
    """
    model = Room
    template_name = 'room/room.html'
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        """
        This method is used to pass extra context.
        """
        context = super(RoomDetailView, self).get_context_data(**kwargs)
        context.update({
            'me': self.request.user,
            'room_name': self.object.name,
            'chats': Chat.objects.filter(room=self.kwargs['pk'])
        })
        return context
