import json
import asyncio
import time

from channels.consumer import AsyncConsumer,SyncConsumer


class ChatConsumer(SyncConsumer):
    def websocket_connect(self, message):
        print("connected",message)
        self.send({
            "type": "websocket.accept",
        })
        room_name = self.scope['url_route']['kwargs']['room_name']
        print(room_name)
        self.send({
            "type": "websocket.send",
            "text":json.dumps({
                'message':'This is a test'
            }),
        })

    def websocket_receive(self, message):
        print("receive",message)


    def websocket_disconnect(self, message):
        print("disconnected",message)

