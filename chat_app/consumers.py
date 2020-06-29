from channels.generic.websocket import AsyncWebsocketConsumer
import json


class MessagesListConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "chat_page", self.channel_name
        )
        await self.accept()
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "chat_page", self.channel_name
        )
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        await self.channel_layer.group_send(
            "chat_page",{
                "type" : "chat.message",
                "message" : text_data_json["message"],
                "sender" : self.scope['user'].username,
        })
    
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message" : event["message"],
            "sender" : event["sender"],
        }))