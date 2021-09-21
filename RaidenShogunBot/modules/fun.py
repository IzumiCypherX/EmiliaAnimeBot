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

@run_async
def runs(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.RUN_STRINGS))


@run_async
def igris(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.IGRIS_STRINGS))
                                                
@run_async
def arise(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(fun_strings.IGRIS_IMG), caption=f'*Command Me {name}*')
     

@run_async
def senpai(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(fun_strings.CUTVEIN_IMG), caption=f'*here I am for you {name} senpai , I will destroy you..*')

@run_async
def truth(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.TRUTH_STRINGS))

@run_async
def insult(update: Update, _):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text(random.choice(fun_strings.INSULT_STRINGS))

@run_async
def dare(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.DARE_STRINGS))
    
@run_async
def sanitize(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(GIF_ID, caption=f'*Sanitizes {name}*')


@run_async
def sanitize(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(
        random.choice(fun_strings.GIFS), caption=f'*Sanitizes {name}*')


@run_async
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
        temp = "@NeoTheKitty scratches {user2}"

    reply = temp.format(
        user1=user1, user2=user2, item=item, hits=hit, throws=throw)

    reply_text(reply, parse_mode=ParseMode.HTML)


@run_async
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


@run_async
def roll(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(range(1, 7)))


@run_async
def toss(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(fun_strings.TOSS))


@run_async
def shrug(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text(r"¯\_(ツ)_/¯")


@run_async
def bluetext(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text(
        "/BLUE /TEXT\n/MUST /CLICK\n/I /AM /A /STUPID /ANIMAL /THAT /IS /ATTRACTED /TO /COLORS"
    )


@run_async
def rlg(update: Update, context: CallbackContext):
    eyes = random.choice(fun_strings.EYES)
    mouth = random.choice(fun_strings.MOUTHS)
    ears = random.choice(fun_strings.EARS)

    if len(eyes) == 2:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[1] + ears[1]
    else:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[0] + ears[1]
    update.message.reply_text(repl)


@run_async
def decide(update: Update, context: CallbackContext):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.DECIDE))


@run_async
def table(update: Update, context: CallbackContext):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.TABLE))

__help__ = """
 • `/runs`*:* reply a random string from an array of replies
 • `/slap`*:* slap a user, or get slapped if not a reply 🌝
 • `/shrug`*:* get shrug XD
 • `/table`*:* get flip/unflip :v
 • `/bluetext`*:* check urself :V
 • `/rlg`*:* Join ears,nose,mouth and create an emo ;-;
 • `/shout <keyword>`*:* write anything you want to give loud shout
 • `/weebify <text>`*:* returns a weebified text
 • `/sanitize`*:* always use this before `/pat` or any contact
 • `/pat`*:* pats a user, or get patted (^-^)
 • `/uwu`*:* gives a UwU reaction with girf or sticker
 • `/owo`*:* gives a OwO reaction with gif or sticket
  - - - - - - - - - -
• *Games* 🎲 *:*
 • `/truth`*:* Get ready to reveal a surprising truth🤫
 • `/dare`*:* A dare is on way 😈
 • `/igris`*:* Summon up IGRIS
 • `/insult`*:* Insult the person
 • `/decide`*:* Randomly answers yes/no/maybe/idk
 • `/toss`*:* Tosses A coin
 • `/roll`*:* Roll a dice & get you a number
 • `/senpai`*:* call Yumeko senpai to help you 
"""

INSULT_HANDLER = DisableAbleCommandHandler("insult", insult)
ARISE_HANDLER = DisableAbleCommandHandler("arise", arise)   
SENPAI_HANDLER = DisableAbleCommandHandler("senpai", senpai)                                   
IGRIS_HANDLER = DisableAbleCommandHandler("igris", igris)
TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)
SANITIZE_HANDLER = DisableAbleCommandHandler("sanitize", sanitize)
RUNS_HANDLER = DisableAbleCommandHandler("runs", runs)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap)
PAT_HANDLER = DisableAbleCommandHandler("pat", pat)
ROLL_HANDLER = DisableAbleCommandHandler("roll", roll)
TOSS_HANDLER = DisableAbleCommandHandler("toss", toss)
SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug)
BLUETEXT_HANDLER = DisableAbleCommandHandler("bluetext", bluetext)
RLG_HANDLER = DisableAbleCommandHandler("rlg", rlg)
DECIDE_HANDLER = DisableAbleCommandHandler("decide", decide)
TABLE_HANDLER = DisableAbleCommandHandler("table", table)

dispatcher.add_handler(INSULT_HANDLER)
dispatcher.add_handler(ARISE_HANDLER)     
dispatcher.add_handler(SENPAI_HANDLER)                                     
dispatcher.add_handler(IGRIS_HANDLER)
dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(SANITIZE_HANDLER)
dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(PAT_HANDLER)
dispatcher.add_handler(ROLL_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(BLUETEXT_HANDLER)
dispatcher.add_handler(RLG_HANDLER)
dispatcher.add_handler(DECIDE_HANDLER)
dispatcher.add_handler(TABLE_HANDLER)

__mod_name__ = "Fun"
__command_list__ = [
    "runs", "slap", "roll", "toss", "shrug", "bluetext", "rlg", "decide",
    "table", "pat", "sanitize", "senpai"
]
__handlers__ = [
    RUNS_HANDLER,IGRIS_HANDLER,ARISE_HANDLER,SENPAI_HANDLER,TRUTH_HANDLER, DARE_HANDLER, SLAP_HANDLER, PAT_HANDLER, ROLL_HANDLER, TOSS_HANDLER,
    SHRUG_HANDLER, BLUETEXT_HANDLER, RLG_HANDLER, DECIDE_HANDLER, TABLE_HANDLER,INSULT_HANDLER, 
    SANITIZE_HANDLER
]
