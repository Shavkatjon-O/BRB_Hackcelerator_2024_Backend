import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Message, Chat


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Extract chat_id from URL route
        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.room_group_name = f"chat_{self.chat_id}"

        # Ensure channel_layer is available
        if self.channel_layer is None:
            await self.close()
            return

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        # Notify users about the new connection
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "user_status", "status": "Online"}
        )

    async def disconnect(self, close_code):
        # Leave room group
        if self.channel_layer is None:
            return

        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

        # Notify users about the disconnection
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "user_status", "status": "Offline"}
        )

    async def receive(self, text_data):
        # Process incoming message
        text_data_json = json.loads(text_data)
        message = text_data_json.get("message", "")
        user_id = text_data_json.get("user_id")

        # Retrieve chat and user
        chat = await database_sync_to_async(Chat.objects.get)(id=self.chat_id)
        user = await database_sync_to_async(User.objects.get)(id=user_id)

        # Save the message to the database
        await database_sync_to_async(Message.objects.create)(
            chat=chat, user=user, content=message
        )

        # Broadcast the message to the chat group
        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "chat_message", "message": message, "user": user.username},
        )

    async def chat_message(self, event):
        # Handle incoming message
        message = event["message"]
        user = event["user"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, "user": user}))

    async def user_status(self, event):
        # Handle user status update
        status = event["status"]

        # Send status update to WebSocket
        await self.send(text_data=json.dumps({"status": status}))
