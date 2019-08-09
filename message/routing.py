# message/routing.py
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/message/<str:room_name>/', consumers.ChatConsumer),
]
