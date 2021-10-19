#!/usr/bin/env python
# -*- coding=utf-8 -*-

import os
import PIL
import time
import random
import settings
import instabot
import instalooter.looters
from PIL import Image


class my_bot():
    def __init__(self):
        self.tmpbot = instabot.Bot()
        self.tmpbot.login(username="user", password="pass")

    def download_memes(self, hashtag: str, count: int):
        loot = instalooter.looters.HashtagLooter(hashtag)
        try:
            os.stat(settings.directory)
        except:
            os.mkdir(settings.directory)
        loot.download_pictures("memes", media_count=count)

    def create_meme(self, image: str):
        marcadeagua = Image.open("marcadeagua.png")
        try:
            meme = Image.open(f"{settings.directory}//{image}")
        except PIL.UnidentifiedImageError:
            pass
        x, y = meme.size
        size = 60
        meme.paste(marcadeagua.resize((settings.smarca, settings.smarca)),
                   (x-settings.smarca, y-settings.smarca))
        meme.save("meme.jpg")

    def upload_memes(self):
        self.tmpbot.logger.info(
            f"Fotos por subir {len(os.listdir(settings.directory))}")
        self.tmpbot.logger.info(
            f"Dias por foto {len(os.listdir(settings.directory))/50}")
        for x in os.listdir(settings.directory):
            if x[-4:] == ".mp4":
                try:
                    self.tmpbot.upload_video(
                        f"{settings.directory}//{x}", f"{random.choice(settings.opinion)}\n\n----------ignorar--------\n{random.choice(settings.hashtags)}")
                    #os.remove(f"{settings.directory}//{x}")
                    #os.remove(f"{settings.directory}//{x}.jpg")
                    #os.remove(f"{settings.directory}//{x}.CONVERTED.mp4.REMOVE_ME")
                except Exception:
                    continue
            else:
                self.create_meme(x)
                self.tmpbot.upload_photo(
                    f"meme.jpg", caption=f"{random.choice(settings.opinion)}\n\n----------ignorar--------\n{random.choice(settings.hashtags)}")
                os.remove(f"{settings.directory}//{x}")
                try:
                    os.remove(f"meme.jpg.REMOVE_ME")
                except FileNotFoundError:
                    self.upload_memes()
            print("Esperando una hora")
            time.sleep(10)

    def follow_persons(self):
        #[bot.get_username_from_user_id(x) for x in bot.get_user_followers("adrian_dct")]
        for x in range(12):
            self.tmpbot.follow(self.usuarios[x])
            self.tmpbot.logger.info(
                f"EL bot acaba de seguir a {self.tmpbot.get_username_from_user_id(self.usuarios[x])}")
            self.usuarios.pop(x)


def main():
    bot = my_bot()
    while True:
        print("[ ok ] Pulsa Ctrl + C para salir ")
        bot.upload_memes()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Hastal la proxima :D")
        os.remove("config")
