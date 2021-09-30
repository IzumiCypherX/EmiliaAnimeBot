# Credits to @TheHamkerCat

import os
import re

import aiofiles
from pyrogram import filters

from EmiliaAnimeBot import pgram as app
from EmiliaAnimeBot.pyroerror import capture_err
from EmiliaAnimeBot.utils.keyboard import ikb
from EmiliaAnimeBot.utils.pastebin import paste

__mod_name__ = "Paste"
__help__ = "❍`/paste` *:* To Paste Replied Text Or Document To A Pastebin"
pattern = re.compile(
    r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$"
)


@app.on_message(filters.command("paste") & ~filters.edited)
@capture_err
async def paste_func(_, message):
    if not message.reply_to_message:
        return await message.reply("Reply To A Message With /paste")
    r = message.reply_to_message

    if not r.text and not r.document:
        return await message.reply(
            "Only text and documents are supported."
        )

    m = await message.reply("Pasting...")

    if r.text:
        content = str(r.text)
    elif r.document:
        if r.document.file_size > 40000:
            return await m.edit(
                "You can only paste files smaller than 40KB."
            )
        if not pattern.search(r.document.mime_type):
            return await m.edit("Only text files can be pasted.")
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)

    link = await paste(content)
    kb = ikb({"Paste Link": link})
    try:
        await message.reply_photo(
            photo=link, quote=False, reply_markup=kb
        )
    except Exception:
        await message.reply("Here's your paste", reply_markup=kb)
    await m.delete()