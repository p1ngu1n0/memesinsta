#!/usr/bin/env python
# -*- coding=utf-8 -*-

import os
import time
import random
import settings
import instabot
import instalooter.looters
from PIL import Image


class my_bot():
    def __init__(self):
        self.tmpbot = instabot.Bot()
        self.tmpbot.login(username=settings.user, password=settings.password)

    def download_memes(self, hashtag: str, count: int):
        loot = instalooter.looters.HashtagLooter(hashtag)
        try:
            os.stat(settings.directory)
        except:
            os.mkdir(settings.directory)
        loot.download_pictures("memes", media_count=count)

    def create_meme(self, image: str):
        marcadeagua = Image.open("marcadeagua.png")
        meme = Image.open(f"{settings.directory}\\{image}")
        x, y = meme.size
        size = 60
        meme.paste(marcadeagua.resize((settings.smarca, settings.smarca)),
                   (x-settings.smarca, y-settings.smarca))
        meme.save("meme.jpg")

    def upload_memes(self):
        for x in os.listdir(settings.directory):
            self.create_meme(x)
            self.tmpbot.upload_photo(f"meme.jpg", caption=settings.comentario)
            time.sleep(settings.delay)
            os.remove(f"meme.jpg.REMOVE_ME")
            os.remove(f"{settings.directory}\\{x}")


def main():
    bot = my_bot()
    while True:
        bot.download_memes(settings.hashtag, settings.cout_images)
        bot.upload_memes()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Hastal la proxima :D")
        