import json

from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
from channels.db import database_sync_to_async

from channels.generic.websocket import AsyncWebsocketConsumer
from django.db.models.signals import post_save

from . models import *

data = machine_data.objects.filter(machine_id="ABD2").values().last()
print('data',data)

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket connected....',event)
        self.send({
            'type':'websocket.accept',
        })


    def websocket_receive(self,event):
        print('message received...',event)
        print(event['text'])
        self.data = machine_data.objects.filter(machine_id="ABD2").values().last()
        print('data',self.data)
        # self.send(text_data=str(self.data))
        self.send({
            'type': 'websocket.send',
            'text': str(self.data)
        })

        for i in range(50):

            self.send({
                'type':'websocket.send',
                'text': str(i)
            })
            sleep(1)


    def websocket_disconnect(self,event):
        print('websocket Disconnected...',event)
        raise StopConsumer()








class MyAsyncConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self,event):

        print('websocket connected....', event)
        # await self.send({
        #         'type': 'websocket.accept',
        #      })
        await self.accept()
        self.send_data = True

        await self.send_updated_data()




    async def send_updated_data(self):
        while self.send_data:
            data = await self.get_data_from_database()
            data_str = json.dumps(data)

            await self.send(text_data=data_str)

            await asyncio.sleep(2)

        # data = await self.get_data_from_database()
        # print('data', data)
        # data_str = json.dumps(data)
        # print('data_str', data_str)
        # print('data_str', type(data_str))
        #
        # await self.send(text_data=data_str)

        # await self.send({
        #     "type": 'websocket.send',
        #     "text": data_str
        # })

    @database_sync_to_async
    def get_data_from_database(self):
        # data = 'kavya'
        # data = machine_data.objects.filter(machine_id="ABD2")
        data = machine_data.objects.filter(machine_id="ABD1").values().last()

        print('get_data', data)

        return data

    async def websocket_receive(self,event):
        print('message received from client...',event)
        print(event['text'])
        # for i in range(50):
        #     await self.send(text_data=str(i))
        #     await asyncio.sleep(1)
    #     data = await self.get_data_from_database()
    #     print('data', data)
    #     data_str = json.dumps(data)
    #     print('data_str', data_str)
    #     print('data_str', type(data_str))
    #
    #     await self.send(text_data=data_str)
    #
    #
    #     # await self.send({
    #     #     "type": 'websocket.send',
    #     #     "text": data_str
    #     # })
    #
    # @database_sync_to_async
    # def get_data_from_database(self):
    #     # data = 'kavya'
    #     # data = machine_data.objects.filter(machine_id="ABD2")
    #     data = machine_data.objects.filter(machine_id="ABD1").values().last()
    #
    #     print('get_data', data)
    #
    #     return data

            # await self.send(
            #     # 'type': 'websocket.send',
            #     text= str(i)
            # )
            # data = {
            #     'type': 'websocket.send',
            #     'text': str(i)
            # }
        # await self.send(json.dumps(data))


    async def websocket_disconnect(self,event):
        print('websocket Disconnected...',event)
        # raise StopConsumer()




#ws://43.204.20.245:8000/ws/ac/



# amac_soln/maithri_app
#  await asyncio.sleep(1)