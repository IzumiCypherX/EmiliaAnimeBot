
import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import SaitamaRobot.modules.nekostrings as neko_strings
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from SaitamaRobot.modules.helper_funcs.extraction import extract_user



@run_async
def nyaa(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        neko_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(neko_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    nyaa_type = random.choice(("Text", "Gif"))
    if nyaa_type == "Gif":
        try:
            temp = random.choice(neko_strings.NEKO_GIF)
            reply_to.reply_animation(temp)
        except BadRequest:
            cuddle_type = "Text"

    if cuddle_type == "Text":
        temp = random.choice(love_strings.CUDDLE_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)
