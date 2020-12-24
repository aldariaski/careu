from django.urls import re_path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/messages/(?P<username>\w+)/$', consumers.ChatConsumer.as_asgi())
]
