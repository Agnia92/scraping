import requests
import re
from config import YOUR_LOGIN, YOUR_PASSWORD, URL


class Scrapping:
    def __init__(self):
        self.login = YOUR_LOGIN
        self.password = YOUR_PASSWORD
        self.url = URL
        self.current_title = ""
        self.session = self.to_login()

    def to_login(self):
        url = self.url + "/account/login"
        payload = {"form_type": "customer_login",
                   "customer[email]": self.login,
                   "customer[password]": self.password}
        session = requests.Session()
        session.post(url, data=payload)
        return session

    def scrap(self):
        titles = {}
        blog = self.session.get(self.url + "/blogs/tesmanian-blog")
        text = blog.text
        result = re.findall(r'<a href="/blogs/tesmanian-blog/.*</a></h2>', text)
        for el in result:
            holder = el.split('">')
            if holder[1][:-9] == self.current_title:
                print("Has not new titles")
                break
            titles[holder[1][:-9]] = self.url + holder[0][9:]
            self.current_title = list(titles.keys())[0]
        for link, article in titles.items():
            return article+" - "+link
