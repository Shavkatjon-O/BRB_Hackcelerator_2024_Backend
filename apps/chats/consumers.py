import json
from channels.generic.websocket import AsyncWebsocketConsumer
import logging

logger = logging.getLogger(__name__)


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.chat_group_name = f"chat_{self.chat_id}"

        # Join room group
        await self.channel_layer.group_add(self.chat_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.chat_group_name, self.channel_name)

    async def chat_message(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "id": event.get("id"),
                    "user": event.get("user"),
                    "chat": event.get("chat"),
                    "text": event.get("text"),
                    "created_at": event.get("created_at", ""),
                }
            )
        )
