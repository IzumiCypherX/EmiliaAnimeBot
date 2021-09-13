# To all kangers, You Dare kang this file and come asking for Not working in Tangent
# this is all a test

from pyrogram import filters

from EmiliaAnimeBot import USERBOT_PREFIX, DEV_USERS, emiliaub



@emiliaub.on_message(
    filters.command("meowtest", prefixes=USERBOT_PREFIX)
    & filters.user(DEV_USERS)
       await message.reply_text("I'm already up!!")
)
