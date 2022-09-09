from asyncio.windows_events import NULL
import json
from urllib import response

from channels.generic.websocket import WebsocketConsumer
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connected', event)
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self, event):
        print('receive', event)
        print("123")
        recieved_data = json.loads(event['text'])
        print(recieved_data)
        msg = recieved_data.get('message')
        print(msg)
        if not  msg :
            return False
       
        
        response={
             
            'message':msg
        }
        
      
        await self.send({
            'type':'websocket.send',
            'text':json.dumps(response)
        })

    async def websocket_disconnect(self, event):
        print('disconnected', event)

    