from asyncio import gather, sleep

from pyrogram import filters
from pyrogram.types import Message
from aiohttp import ClientSession
from Python_ARQ import ARQ

from RaidenShogunBot import pgram as app
from RaidenShogunBot.pyrogramee.pluginshelper import edit_or_reply as eor
from RaidenShogunBot.pyrogramee.errors import capture_err
from RaidenShogunBot.utils.filter_groups import chatbot_group
from RaidenShogunBot.arqclient import arq
from RaidenShogunBot import BOT_ID

__mod_name__ = "ChatBot"
__help__ = """
/chatbot [ENABLE|DISABLE] To Enable Or Disable ChatBot In Your Chat.
"""

active_chats_bot = []

async def chat_bot_toggle(db, message: Message):
    status = message.text.split(None, 1)[1].lower()
    chat_id = message.chat.id
    if status == "enable":
        if chat_id not in db:
            db.append(chat_id)
            text = "Chatbot Enabled!"
            return await eor(message, text=text)
        await eor(message, text="ChatBot Is Already Enabled.")
    elif status == "disable":
        if chat_id in db:
            db.remove(chat_id)
            return await eor(message, text="Chatbot Disabled!")
        await eor(message, text="ChatBot Is Already Disabled.")
    else:
        await eor(
            message, text="**Usage:**\n/chatbot [ENABLE|DISABLE]"
        )


# Enabled | Disable Chatbot


@app.on_message(filters.command("chatbot") & ~filters.edited)
@capture_err
async def chatbot_status(_, message: Message):
    if len(message.command) != 2:
        return await eor(
            message, text="**Usage:**\n/chatbot [ENABLE|DISABLE]"
        )
    await chat_bot_toggle(active_chats_bot, message)


async def lunaQuery(query: str, user_id: int):
    luna = await arq.luna(query, user_id)
    return luna.result


async def type_and_send(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    response, _ = await gather(lunaQuery(query, user_id), sleep(3))
    await message.reply_text(response)
    await message._client.send_chat_action(chat_id, "cancel")


@app.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded,
    group=chatbot_group,
)
@capture_err
async def chatbot_talk(_, message: Message):
    if message.chat.id not in active_chats_bot:
        return
    if not message.reply_to_message:
        return
    if not message.reply_to_message.from_user:
        return
    if message.reply_to_message.from_user.id != BOT_ID:
        return
    await type_and_send(message)
