from django.contrib import admin

# Register your models here.

from apps.chats.models import Chat, Message

admin.site.register(Chat)
admin.site.register(Message)
