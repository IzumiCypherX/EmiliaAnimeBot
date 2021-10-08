import os
from datetime import datetime as dt
from random import choice
from shutil import rmtree

import moviepy.editor as m
import pytz
import requests
from bs4 import BeautifulSoup as b
from pyUltroid.functions.google_image import googleimagesdownload
from EmiliaAnimeBot.events import register
from telethon import events
from EmiliaAnimeBot import telethn as bot
from EmiliaAnimeBot import dispatcher

@register(pattern="^/wall (.*)")
async def wall(event):
    inp = event.pattern_match.group(1)
    if not inp:
        return await event.reply("Give me something to search..")
    x = await event.reply("Processing Keep Patience...")
    query = f"hd {inp}"
    gi = googleimagesdownload()
    args = {
        "keywords": query,
        "limit": 10,
        "format": "jpg",
        "output_directory": "./resources/downloads/",
    }
    gi.download(args)
    xx = choice(os.listdir(os.path.abspath(f"./resources/downloads/{query}/")))
    await event.client.send_file(event.chat_id, f"./resources/downloads/{query}/{xx}")
    rmtree(f"./resources/downloads/{query}/")
    await x.delete()
