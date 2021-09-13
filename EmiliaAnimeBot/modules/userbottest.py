from EmiliaAnimeBot import emiliaub, DEV_USERS, USERBOT_PREFIX
from pyrogram import filters


@emiliaub.on_message(filters.command("alive", prefixes = USERBOT_PREFIX) & filters.users(DEV_USERS))
async def alive(_, message: Message):
    txt = "hello"
    await message.edit(txt)
        


     
