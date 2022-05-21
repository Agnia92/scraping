from config import BOT_TOKEN, CHANNEL_ID
import requests


class Bot:
    def __init__(self):
        self.token = BOT_TOKEN
        self.channel_id = CHANNEL_ID
        self.message = ""

    def send_to_chanel(self, text):
        self.message = text
        url = "https://api.telegram.org/bot" + self.token
        method = url + "/sendMessage"
        r = requests.post(method, data={
            "chat_id": self.channel_id,
            "text": self.message
        })
        if r.status_code != 200:
            raise Exception("post_text error")
