from mtranslate import translate
from SaitamaRobot import telethn
import json
import requests
from SaitamaRobot.events import register
from telethon import *
from telethon.tl import functions
import os
import urllib.request
from typing import List
from typing import Optional
from telethon.tl import types
from telethon.tl.types import *


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):

        return isinstance(
            (await
             oko(functions.channels.GetParticipantRequest(chat,
                                                           user))).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerChat):

        ui = await oko.get_peer_id(user)
        ps = (await oko(functions.messages.GetFullChatRequest(chat.chat_id)
                         )).full_chat.participants.participants
        return isinstance(
            next((p for p in ps if p.user_id == ui), None),
            (types.ChatParticipantAdmin, types.ChatParticipantCreator),
        )
    return None


@register(pattern="^/tr (.*)")
async def _(event):

    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    
    try:
        translated = translate(text,lan,"auto")
        await event.reply(translated)
    except Exception as exc:
        print(exc)
        await event.reply("**Server Error !**\nTry Again.")

help = """
- /tr [List of Language Codes](t.me/fateunionupdates/32) :- as reply to a long message.
"""
__mod_name__= "Translator"
