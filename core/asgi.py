import django

django.setup()

import os
import environ
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from apps.chats.consumers import ChatConsumer

env = environ.Env()
env.read_env(".env")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    path("ws/chat/<int:chat_id>/", ChatConsumer.as_asgi()),
                ]
            )
        ),
    }
)
