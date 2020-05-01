import os
import requests

class RequestsService:
    def __init__(self, bot_token):
        self.request_url = 'https://api.telegram.org/bot' + bot_token

    def send_message(self, chat_id, message):
        data = {
            'chat_id': chat_id,
            'text': message
        }

        return requests.post(self.request_url + '/sendMessage', json=data)

    def send_video(self, chat_id, video_name):
        data = { 'video': open(video_name, 'rb') }

        return requests.post(self.request_url + '/sendVideo' + '?chat_id={}'.format(chat_id), files=data)
