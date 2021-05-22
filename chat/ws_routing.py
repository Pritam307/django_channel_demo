from django.urls import re_path, path
from chat.consumers import ChatConsumer
from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<room_name>', consumers.ChatConsumer.as_asgi()),
]