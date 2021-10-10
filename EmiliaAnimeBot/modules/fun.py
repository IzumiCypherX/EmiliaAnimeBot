import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import EmiliaAnimeBot.modules.fun_strings as fun_strings
from EmiliaAnimeBot import dispatcher
from EmiliaAnimeBot.modules.disable import DisableAbleCommandHandler
from EmiliaAnimeBot.modules.helper_funcs.chat_status import (is_user_admin)
from EmiliaAnimeBot.modules.helper_funcs.extraction import extract_user

GIF_ID = 'CgACAgUAAx0EVmwfqQACElhfo3yZv1njCC11INcQSAi4UlN8vwACqwADg_8wVeGSv41OYU6zHgQ'

PHOTO = 'https://i.imgur.com/UjiCJhZ.jpg'

run_async=True
def runs(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.RUN_STRINGS))


run_async=True
def truth(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.TRUTH_STRINGS))

run_async=True
def insult(update: Update, _):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text(random.choice(fun_strings.INSULT_STRINGS))

run_async=True
def dare(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.DARE_STRINGS))

run_async=True
def slap(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat

    reply_text = message.reply_to_message.reply_text if message.reply_to_message else message.reply_text

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == bot.id:
        temp = random.choice(fun_strings.SLAP_EMILIA_TEMPLATES)

        if isinstance(temp, list):
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):
                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(
                    chat.id,
                    message.from_user.id,
                    until_date=mutetime,
                    permissions=ChatPermissions(can_send_messages=False))
            reply_text(temp[0])
        else:
            reply_text(temp)
        return

    if user_id:

        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(slapped_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    temp = random.choice(fun_strings.SLAP_TEMPLATES)
    item = random.choice(fun_strings.ITEMS)
    hit = random.choice(fun_strings.HIT)
    throw = random.choice(fun_strings.THROW)

    if update.effective_user.id == 1096215023:
        temp = "The Catto scratches {user2}"

    reply = temp.format(
        user1=user1, user2=user2, item=item, hits=hit, throws=throw)

    reply_text(reply, parse_mode=ParseMode.HTML)


run_async=True
def pat(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        patted_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(patted_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    pat_type = random.choice(("Text", "Gif", "Sticker"))
    if pat_type == "Gif":
        try:
            temp = random.choice(fun_strings.PAT_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            pat_type = "Text"

    if pat_type == "Sticker":
        try:
            temp = random.choice(fun_strings.PAT_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            pat_type = "Text"

    if pat_type == "Text":
        temp = random.choice(fun_strings.PAT_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)


run_async=True
def roll(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(range(1, 7)))


run_async=True
def toss(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(fun_strings.TOSS))


run_async=True
def shrug(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text(r"¯\_(ツ)_/¯")


run_async=True
def rlg(update: Update, context: CallbackContext):
    eyes = random.choice(fun_strings.EYES)
    mouth = random.choice(fun_strings.MOUTHS)
    ears = random.choice(fun_strings.EARS)

    if len(eyes) == 2:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[1] + ears[1]
    else:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[0] + ears[1]
    update.message.reply_text(repl)


run_async=True
def decide(update: Update, context: CallbackContext):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.DECIDE))


run_async=True
def table(update: Update, context: CallbackContext):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.TABLE))

__help__ = """
 ❍ `/runs`*:* Reply a random string from an array of replies
 ❍ `/slap`*:* Slap a user, or get slapped if not a reply 🌝
 ❍ `/shrug`*:* Get shrug XD
 ❍ `/table`*:* Get flip/unflip :v
 ❍ `/rlg`*:* Join ears,nose,mouth and create an emo ;-;
 ❍ `/shout <keyword>`*:* Write anything you want to give loud shout
 ❍ `/weebify <text>`*:* Returns a weebified text
 ❍ `/pat`*:* Pats a user, or get patted (^-^)
  - - - - - - - - - -
❍ *Games* 🎲 *:*
 ❍ `/truth`*:* Get ready to reveal a surprising truth🤫
 ❍ `/dare`*:* A dare is on way 😈
 ❍ `/insult`*:* Insult the person
 ❍ `/decide`*:* Randomly answers yes/no/maybe/idk
 ❍ `/toss`*:* Tosses A coin
 ❍ `/roll`*:* Roll a dice & get you a number
"""

RUNS_HANDLER = DisableAbleCommandHandler("runs", runs)
TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)
INSULT_HANDLER = DisableAbleCommandHandler("insult", insult)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap)
PAT_HANDLER = DisableAbleCommandHandler("pat", pat)
ROLL_HANDLER = DisableAbleCommandHandler("roll", roll)
TOSS_HANDLER = DisableAbleCommandHandler("toss", toss)
SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug)
RLG_HANDLER = DisableAbleCommandHandler("rlg", rlg)
DECIDE_HANDLER = DisableAbleCommandHandler("decide", decide)
TABLE_HANDLER = DisableAbleCommandHandler("table", table)

dispatcher.add_handler(INSULT_HANDLER)
dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(PAT_HANDLER)
dispatcher.add_handler(ROLL_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(RLG_HANDLER)
dispatcher.add_handler(DECIDE_HANDLER)
dispatcher.add_handler(TABLE_HANDLER)

__mod_name__ = "Fun"
__command_list__ = [
    "runs", "slap", "roll", "toss", "shrug", "rlg", "decide",
    "table", "pat", "dare", "truth", "insult"
]
__handlers__ = [
    RUNS_HANDLER, TRUTH_HANDLER, DARE_HANDLER, SLAP_HANDLER, PAT_HANDLER, ROLL_HANDLER, TOSS_HANDLER,
    SHRUG_HANDLER, RLG_HANDLER, DECIDE_HANDLER, TABLE_HANDLER, INSULT_HANDLER,
]
