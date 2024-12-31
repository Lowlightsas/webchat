# chat/routing.py
from django.urls import path
from .consumers import ChatroomConsumer

websocket_urlpatterns = [
    path('ws/chatroom/', ChatroomConsumer.as_asgi()),
]