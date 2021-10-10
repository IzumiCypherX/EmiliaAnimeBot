from time import sleep
from typing import Optional, List
from telegram import TelegramError
from telegram import Update
from telegram.error import BadRequest
from telegram.ext import Filters, CommandHandler
from telegram.ext.dispatcher import run_async, CallbackContext

import random
import EmiliaAnimeBot.modules.sql.users_sql as sql
from EmiliaAnimeBot.modules.helper_funcs.filters import CustomFilters
from EmiliaAnimeBot import dispatcher, OWNER_ID, LOGGER
from EmiliaAnimeBot.modules.disable import DisableAbleCommandHandler
USERS_GROUP = 4


@run_async
def snipe(update: Update, context: CallbackContext):
    args = context.args
    bot = context.bot
    try:
        chat_id = str(args[0])
        del args[0]
    except TypeError:
        update.effective_message.reply_text(
            "Please give me a chat to echo to!")
    to_send = " ".join(args)
    if len(to_send) >= 2:
        try:
            bot.sendMessage(int(chat_id), str(to_send))
        except TelegramError:
            LOGGER.warning("Couldn't send to group %s", str(chat_id))
            update.effective_message.reply_text(
                "Couldn't send the message. Perhaps I'm not part of that group?")


__help__ = """

──「 *Sudo only:* 」──
-> /snipe <chatid> <string>
Make me send a message to a specific chat.
"""

__mod_name__ = "Snipe"

SNIPE_HANDLER = CommandHandler(
    "snipe",
    snipe,
    pass_args=True,
    filters=CustomFilters.sudo_filter)

dispatcher.add_handler(SNIPE_HANDLER)

