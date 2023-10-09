import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

max_index = 5
img_ind = 0


class ImageConsumer(WebsocketConsumer):
    current_image_url = "initial_image.jpg"  # Исходная ссылка на изображение

    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        global max_index
        global img_ind
        text_data_json = json.loads(text_data)

        if 'type' in text_data_json and text_data_json['type'] == 'update_image':
            img_ind += 1
            if img_ind > max_index:
                img_ind = 0
            new_image_url = f'static/images/image{img_ind}.jpg'

            if new_image_url:
                ImageConsumer.current_image_url = new_image_url

                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'update_image',
                        'image_url': new_image_url
                    }
                )

    def update_image(self, event):
        image_url = event['image_url']

        self.send(text_data=json.dumps({
            'type': 'update_image',
            'image_url': image_url
        }))
