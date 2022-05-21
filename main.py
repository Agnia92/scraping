from models.telegram import Bot
from models.scrapper import Scrapping
import time


if __name__ == "__main__":
    while True:
        bot = Bot()
        scraper = Scrapping()
        try:
            while True:
                bot.send_to_chanel(scraper.scrap())
                time.sleep(15)
        except:
            print("re-entry")
