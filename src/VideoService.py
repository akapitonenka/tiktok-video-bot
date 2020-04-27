import os
import requests

class VideoService:
    def __init__(self):
        self.video_name = ''

    def save_video(self, video_url):
        first_index = 23
        last_index = 33

        self.video_name = video_url[first_index : last_index] + '.mp4'

        r = requests.get(video_url, stream=True)

        with open(self.video_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=255):
                f.write(chunk)

    def delete_video(self):
        os.remove(self.video_name)