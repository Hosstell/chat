from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

USER_LIST = {}


class ChatConsumer(WebsocketConsumer):
    group_chat_name = 'common_chat'

    def connect(self):
        print('Соединение')
        print('Название канала:', self.channel_name)

        _id = self.scope['cookies'].get('_ym_uid')
        if _id in USER_LIST:
            USER_LIST[_id]['online'] = True
            self.send_users_list()

        async_to_sync(self.channel_layer.group_add)(
            self.group_chat_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_chat_name,
            self.channel_name
        )

        _id = self.scope['cookies']['_ym_uid']
        USER_LIST[_id]['online'] = False

        self.send_users_list()

    def send_users_list(self):
        users_list = list(USER_LIST.values())
        users_list = list(filter(lambda x: x['online'], users_list))

        async_to_sync(self.channel_layer.group_send)(
            self.group_chat_name,
            {
                'type': 'user_list',
                'message': users_list
            }
        )

    def receive(self, text_data):
        self.create_user()
        text_data_json = json.loads(text_data)

        if text_data_json['type'] == 'myData':
            sex_format = {
                'Мужской': 'M',
                'Женский': 'F'
            }
            _id = self.scope['cookies'].get('_ym_uid')
            USER_LIST[_id]['name'] = text_data_json['data']['name']
            USER_LIST[_id]['sex'] = sex_format[text_data_json['data']['sex']]
            self.send_users_list()

        if text_data_json['type'] == 'message':
            _id = self.scope['cookies']['_ym_uid']

            async_to_sync(self.channel_layer.group_send)(
                self.group_chat_name,
                {
                    'type': 'message',
                    'message': {
                        'user': USER_LIST[_id],
                        'text': text_data_json['data']
                    }
                }
            )

        if text_data_json['type'] == 'getMe':
            _id = self.scope['cookies'].get('_ym_uid')

            self.send(text_data=json.dumps({
                'type': 'my_data',
                'message': {
                    'name': USER_LIST[_id]['name'],
                    'sex': USER_LIST[_id]['sex'],
                }
            }))

        if text_data_json['type'] == 'online':
            _id = self.scope['cookies']['_ym_uid']
            USER_LIST[_id]['online'] = True
            self.send_users_list()

    def create_user(self):
        _id = self.scope['cookies'].get('_ym_uid')

        if _id not in USER_LIST:
            USER_LIST[_id] = {
                'name': '',
                'sex': 'M',
                'online': True
            }

    def message(self, data):
        self.send(text_data=json.dumps(data))

    def user_list(self, data):
        self.send(text_data=json.dumps(data))

