from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from chat_app import consumers


application = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(
        URLRouter([
            re_path(r'', consumers.MessagesListConsumer)
        ])
    ),
})