from flask import Flask, request, jsonify
import requests
import os
from config import BOT_TOKEN, CHANNEL_ID
from TikTokParser import TikTokParser
from RequestsService import RequestsService
from VideoService import VideoService

app = Flask(__name__)

tiktok_parser = TikTokParser()
video_service = VideoService()

message = '<h1>Пацанский бот</h1>'

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()

        if r.get('message', None) == None:
            return message

        requests_service = RequestsService(BOT_TOKEN, CHANNEL_ID)

        video_src = tiktok_parser.get_video_src(r['message']['text'])

        if video_src == None:
            requests_service.send_message('Здесь должна быть ссылка на видос тик тока')

            return message

        video_service.save_video(video_src)

        r = requests_service.send_video(video_service.video_name)

        if r.status_code != 200:
            requests_service.send_message('Случился рофл, попробуй еще раз')

            return message

        video_service.delete_video()

    return message

if __name__ == "__main__":
    app.run()

