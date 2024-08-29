# # """
# # ASGI config for core project.

# # It exposes the ASGI callable as a module-level variable named ``application``.

# # For more information on this file, see
# # https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
# # """

# # import os

# # from django.core.asgi import get_asgi_application

# # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# # application = get_asgi_application()


# import os
# import django

# django.setup()
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from apps.chats.consumers import ChatConsumer
# from django.urls import re_path

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")

# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         "websocket": AuthMiddlewareStack(
#             URLRouter(
#                 [
#                     re_path(r"ws/chat/(?P<chat_id>\d+)/$", ChatConsumer.as_asgi()),
#                 ]
#             )
#         ),
#     }
# )


# asgi.py
import django

django.setup()
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from apps.chats import routing

import environ

env = environ.Env()
env.read_env(".env")

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)),
    }
)
