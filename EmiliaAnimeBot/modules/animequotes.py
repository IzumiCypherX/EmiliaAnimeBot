import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import EmiliaAnimeBot.modules.animemisc_strings as animisc
from EmiliaAnimeBot import dispatcher
from EmiliaAnimeBot.modules.disable import DisableAbleCommandHandler
from EmiliaAnimeBot.modules.helper_funcs.chat_status import (is_user_admin)
from EmiliaAnimeBot.modules.helper_funcs.extraction import extract_user

run_async=True
def quotepics(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(animisc.QUOTES_IMG))

@run_async
def quotetexts(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(animisc.QUOTES_TEXT))

__help__ = """
 ❍ `/quotepic`*:* Sends Random Quote Pictures
 ❍ `/quotetext`*:* Sends Random Qoute Texts
 
"""
QUOTEPICS_HANDLER = DisableAbleCommandHandler("quotepic", quotepics)
QUOTETEXT_HANDLER = DisableAbleCommandHandler("quotetext", quotetexts)

dispatcher.add_handler(QUOTEPICS_HANDLER)
dispatcher.add_handler(QUOTETEXT_HANDLER)

__mod_name__ = "Anime Misc"
__command_list__ = [
    "quotepic", "quotetext"
]
__handlers__ = [
   QUOTEPICS_HANDLER, QUOTETEXT_HANDLER
]
