import json
from django.contrib.auth import get_user_model
from channels.generic.websocket import AsyncWebsocketConsumer
from apps.chats.models import Chat, Message


User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.chat_group_name = f"chat_{self.chat_id}"

        # Join room group
        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        message_text = text_data_json["text"]
        user_id = self.scope["user"].id

        chat = await Chat.objects.get(id=self.chat_id)
        user = await User.objects.get(id=user_id)

        # Save message to the database
        message = Message.objects.create(
            user=user,
            chat=chat,
            text=message_text,
        )

        # Send message to room group
        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                "type": "chat_message",
                "message": message_text,
                "user": user.username,
            },
        )

    async def chat_message(self, event):
        message = event["message"]
        user = event["user"]

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "user": user,
                },
            ),
        )
