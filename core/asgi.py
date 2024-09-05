import os
import environ

from django.urls import path
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

from apps.chats.consumers import ChatConsumer

import django

django.setup()

env = environ.Env()
env.read_env(".env")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    [
                        path("ws/chats/<int:chat_id>/", ChatConsumer.as_asgi()),
                    ],
                ),
            ),
        ),
    },
)
