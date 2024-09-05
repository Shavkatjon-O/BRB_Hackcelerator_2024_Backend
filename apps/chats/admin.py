from django.contrib import admin
from apps.chats.models import Message
from apps.chats.models import Chat

admin.site.register(Message)
admin.site.register(Chat)
