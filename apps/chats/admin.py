from django.contrib import admin
from apps.chats.models import DirectChat, DirectMessage, GroupChat, GroupMessage

admin.site.register(DirectChat)
admin.site.register(DirectMessage)
admin.site.register(GroupChat)
admin.site.register(GroupMessage)
