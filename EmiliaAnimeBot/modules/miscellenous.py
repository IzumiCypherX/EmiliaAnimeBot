from pyrogram import filters
from pyrogram.types import Message

from EmiliaAnimeBot import pgram
from EmiliaAnimeBot.pyrogramee.errors import capture_err


@pgram.on_message(filters.command("webss"))
@capture_err
async def take_ss(_, message: Message):
    try:
        if len(message.command) != 2:
            return await message.reply_text(
                "No URL Provided"
            )
        url = message.text.split(None, 1)[1]
        m = await message.reply_text("**Capturing...**")
        await m.edit("**Sending...**")
        try:
            await message.reply_photo(
                photo=f"https://webshot.amanoteam.com/print?q={url}",
                quote=False,
            )
        except TypeError:
            return await m.edit("No Such Website Found.")
        await m.delete()
    except Exception as e:
        await message.reply_text(str(e))


__mod_name__ = "Misc"

__help__ = """

*Google Funcs*

 ❍ `/google` *:* Perform a google search
 ❍ `/img` *:* Search Google for images and returns them\nFor greater no. of results specify lim, For eg: `/img hello lim=10`
 ❍ `/app` *:* Searches for an app in Play Store and returns its details.
 ❍ `/reverse` *:* Does a reverse image search of the media which it was replied to.

*Data Hiding Funcs*

❍`/encrypt` *:* Encrypts The Given Text
❍`/decrypt` *:* Decrypts Previously Ecrypted Text

*Translation*

❍`tr`*:* Translates a message to the given Language code

*Text-To-Speech*

❍`/tts`*:* Convert text to speech

*Web SS*

❍`/webss`*:* Take a ScreenShot of the Given Website

*Github*

❍`/github`*:* Search a Github Profile

"""
