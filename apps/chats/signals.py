from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import DirectMessage


@receiver(post_save, sender=DirectMessage)
def notify_new_message(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()

        partner = (
            instance.chat.user1
            if instance.user == instance.chat.user2
            else instance.chat.user2
        )

        print(partner)

        # Ensure that the message follows the same structure as the WebSocket consumer
        async_to_sync(channel_layer.group_send)(
            f"chat_{instance.chat.id}",
            {
                "type": "chat_message",  # This triggers the 'chat_message' method in the consumer
                "id": instance.id,  # Include message ID if applicable
                "text": instance.text,
                "created_at": (
                    instance.created_at.isoformat() if instance.created_at else ""
                ),
                "user": {
                    "email": instance.user.email,
                    "first_name": instance.user.first_name,
                    "last_name": instance.user.last_name,
                    "image": (instance.user.image.url if instance.user.image else None),
                },
                "chat": {
                    "id": instance.chat.id,
                    "partner": {
                        "email": partner.email,
                        "first_name": partner.first_name,
                        "last_name": partner.last_name,
                        "image": (partner.image.url if partner.image else None),
                    },
                },
            },
        )
