from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.chat_group_name = f"chat_{self.chat_id}"

        # Join chat room group
        await self.channel_layer.group_add(self.chat_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave chat room group
        await self.channel_layer.group_discard(self.chat_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        sender = self.scope["user"].username

        # Send message to chat room group
        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                "message": message,
                "type": "chat_message",
                "sender": sender,
            },
        )

    # Receive message from chat room group
    async def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "sender": sender,
                },
            ),
        )
