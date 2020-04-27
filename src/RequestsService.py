import os
import requests

class RequestsService:
    def __init__(self, bot_token, chat_id):
        self.request_url = 'https://api.telegram.org/bot' + bot_token
        self.chat_id = chat_id

    def send_message(self, message):
        data = {
            'chat_id': self.chat_id,
            'text': message
        }

        return requests.post(self.request_url + '/sendMessage', json=data)

    def send_video(self, video_name):
        data = { 'video': open(video_name, 'rb') }

        return requests.post(self.request_url + '/sendVideo' + '?chat_id={}'.format(self.chat_id), files=data)
