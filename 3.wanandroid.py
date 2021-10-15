import json

import requests


class WanAndroidSpider():
    def __init__(self):
        self.start_url = "https://wanandroid.com/project/tree/json"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }

    def parse(self):
        response = requests.get(self.start_url, headers=self.headers)
        jsondata = json.loads(response.text)
        datas = jsondata['data']
        for data in datas:
            print(data['name'], data['id'], data['order'])


if __name__ == '__main__':
    wanAndroid = WanAndroidSpider()
    wanAndroid.parse()
