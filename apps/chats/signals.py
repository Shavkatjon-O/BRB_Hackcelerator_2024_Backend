from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import DirectMessage


@receiver(post_save, sender=DirectMessage)
def notify_new_message(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"chat_{instance.chat.id}",
            {
                "type": "chat_message",
                "message": instance.text,
            },
        )
