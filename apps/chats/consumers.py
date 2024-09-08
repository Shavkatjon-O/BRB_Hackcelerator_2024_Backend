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

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message_data = text_data_json.get("message", {})

            user_data = message_data.get("user", {})
            chat_data = message_data.get("chat", {})

            # Broadcast message to the group
            await self.channel_layer.group_send(
                self.chat_group_name,
                {
                    "type": "chat_message",
                    "id": message_data.get("id"),
                    "user": {
                        "email": user_data.get("email", ""),
                        "first_name": user_data.get("first_name", ""),
                        "last_name": user_data.get("last_name", ""),
                        "image": user_data.get("image", ""),
                    },
                    "chat": {
                        "id": chat_data.get("id", ""),
                        "partner": {
                            "email": chat_data.get("partner", {}).get("email", ""),
                            "first_name": chat_data.get("partner", {}).get(
                                "first_name", ""
                            ),
                            "last_name": chat_data.get("partner", {}).get(
                                "last_name", ""
                            ),
                            "image": chat_data.get("partner", {}).get("image", ""),
                        },
                    },
                    "text": message_data.get("text", ""),
                    "created_at": message_data.get("created_at", ""),
                },
            )
        except json.JSONDecodeError:
            logger.error("Error decoding WebSocket message")
        except Exception as e:
            logger.error(f"Error processing WebSocket message: {e}")

    async def chat_message(self, event):
        # Send the event back to the WebSocket
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
