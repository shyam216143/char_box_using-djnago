from asyncio.windows_events import NULL
from email import message
import json
from urllib import response
import channels.layers
from channels.generic.websocket import WebsocketConsumer
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User

from .models import Message, ThreadingTable
channel_layer = channels.layers.get_channel_layer()
class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connected', event)
        user = self.scope['user']
        chat_room = f'user_chatroom_{user.id}'
        self.chat_room = chat_room

        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self, event):
        print('receive', event)
        print("123")
        recieved_data = json.loads(event['text'])
        print(recieved_data)
        msg = recieved_data.get('message')
        sent_by_id = recieved_data.get('sent_by')
        send_to_id = recieved_data.get('send_to')
        thread_id = recieved_data.get('thread_id')
          
        print(msg)
        if not  msg :

            print("error:: empty message")
            return False
       
        sent_by_user= await self.get_user_object(sent_by_id)        
        send_to_user= await self.get_user_object(send_to_id) 
        thread_obj= await self.get_thread(thread_id) 


        if not sent_by_user:
            print("error:: sent by user is incorrect")   

        if not send_to_user:
            print("error:: send to user is incorrect")   
        if not thread_obj:
            print("error:: Thread id is incorrect")   


        await self.create_chat_message(thread_obj,sent_by_user,msg)



        other_user_in_chat_room = f'user_chatroom_{send_to_id}'   
        self_user = self.scope['user'] 

        response={
             
            'message':msg,

            'sent_by':self_user.id,

            'thread_id':thread_id
        }


        await self.channel_layer.group_send(
            other_user_in_chat_room,
            {
                'type':'chat_message',
                'text': json.dumps(response)

            }
        )
        
        await self.channel_layer.group_send(
            self.chat_room,
            {
                'type':'chat_message',
                'text': json.dumps(response)

            }
        )
      
      

    async def websocket_disconnect(self, event):
        print('disconnected', event)
       

    async def chat_message(self, event):
        print('chat_message', event)
        await self.send({
            'type': 'websocket.send',
            'text': event['text'],
        })


    @database_sync_to_async
    def get_user_object(self, user_id):
        qe = User.objects.filter(id = user_id)
        if qe.exists():
            obj = qe.first()

        else:
            obj=None
            
            
        return obj   



    @database_sync_to_async
    def get_thread(self, thread_id):
        qe = ThreadingTable.objects.filter(id = thread_id)
        if qe.exists():
            obj = qe.first()

        else:
            obj=None
            
            
        return obj      



    @database_sync_to_async
    def create_chat_message(self, thread, user, message):
       Message.objects.create(thread=thread, user=user, message=message)
           