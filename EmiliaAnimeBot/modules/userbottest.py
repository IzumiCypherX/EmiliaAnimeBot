from EmiliaAnimeBot import emiliaub, DEV_USERS, USERBOT_PREFIX
from pyrogram import filters
from pyrogram.types import Message


@emiliaub.on_message(filters.command("alive", prefixes = USERBOT_PREFIX) & filters.user(DEV_USERS))
async def alive(_, message: Message):
    txt = "hello"
    await message.edit(txt)
        


     
