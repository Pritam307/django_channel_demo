import json
import asyncio
import time
from asgiref.sync import async_to_sync
from channels.consumer import AsyncConsumer,SyncConsumer


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, message):
        print("connected",message)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.send({
            "type": "websocket.accept"
        })

        await self.send({
            "type":"websocket.send",
            "text": json.dumps({
                'curr_channel':self.channel_name
            })
        })

    async def websocket_receive(self, message):
        print("receive")
        data = message.get('text')
        await self.channel_layer.group_send(
            self.room_name,
            {
                "type":"broadcast_message",
                "text":data,
                "sender_channel_name":self.channel_name
            }
        )
        # await self.emit_to_rest(message)

    async def emit_to_rest(self,event):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )
        self.channel_name = await self.channel_layer.new_channel()
        await self.channel_layer.group_send(
            self.room_name,
            {
                "type": "broadcast_message",
                "text": event.get('text')
            }
        )
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        print(self.channel_name)

    async def broadcast_message(self,event):
        print("recieved msg",event.get('text'))
        await self.send({
            "type": "websocket.send",
            "text": json.dumps({
                "mychannel": event['sender_channel_name'],
                "chat": event['text']
            })
        })

    async def websocket_disconnect(self, message):
        print("disconnected",message)
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

