from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatRoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Extract room name and define the group name
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        
        # Add the channel to the group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the channel from the group on disconnect
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Parse the received JSON data
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '').strip()
        username = text_data_json.get('username', 'Anonymous')

        # Ignore empty messages
        if not message:
            return 

        # Broadcast the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
            }
        )
        
    async def chatroom_message(self, event):
        # Receive the broadcast message and send it to the WebSocket
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))