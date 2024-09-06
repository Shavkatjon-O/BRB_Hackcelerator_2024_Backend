import os
import environ
import django

django.setup()

from django.urls import path
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

from apps.chats.routing import websocket_urlpatterns
from apps.chats.consumers import ChatConsumer


env = environ.Env()
env.read_env(".env")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    websocket_urlpatterns,
                ),
            ),
        ),
    },
)
