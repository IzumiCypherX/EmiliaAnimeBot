from pyrogram import Client
from SaitamaRobot import pgram as bottie

emilia = bottie.get_me()

BOT_ID = emilia.id
BOT_NAME = emilia.first_name + (x.last_name or "")
BOT_USERNAME = emilia.username
BOT_MENTION = emilia.mention
BOT_DC_ID = emilia.dc_id

