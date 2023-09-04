"""This file contains site deployment data such as server names and ports."""

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from chat.forms import LoginForm
from chat.views import RoomCreateView, RoomListView, RoomDetailView, SignupView

app_name = 'chat'

urlpatterns = [

    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='user/login.html', form_class=LoginForm),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('room/create/', RoomCreateView.as_view(), name='room_create'),
    path('room/list/', RoomListView.as_view(), name='room_list'),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room_detail')

]
