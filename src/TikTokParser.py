import requests

class TikTokParser:
    def __init__(self):
        self.headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0' }    

    def get_video_src(self, tiktok_url):
        if tiktok_url.find('https://vm.tiktok.com') == -1:
            return None

        r = requests.get(tiktok_url, headers = self.headers)

        if r.status_code == 200:
            response_text = r.text
        
            video_tag = self.get_video_tag(response_text)

            first_src_index = video_tag.find('https')
            last_src_index = video_tag[first_src_index:].find('"')

            return video_tag[first_src_index:last_src_index]
        
        return None

    def get_video_tag(self, text):
        first_index = text.find('<video')
        last_index = text.find('</video>')

        return text[first_index:last_index]
