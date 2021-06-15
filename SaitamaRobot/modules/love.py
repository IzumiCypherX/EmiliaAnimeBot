import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import SaitamaRobot.modules.love_strings as love_strings
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from SaitamaRobot.modules.helper_funcs.extraction import extract_user



@run_async
def cuddle(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        cuddled_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(cuddled_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    cuddle_type = random.choice(("Text", "Gif"))
    if cuddle_type == "Gif":
        try:
            temp = random.choice(love_strings.CUDDLE_GIF)
            reply_to.reply_animation(temp)
        except BadRequest:
            cuddle_type = "Text"

    if cuddle_type == "Text":
        temp = random.choice(love_strings.CUDDLE_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)


@run_async
def flirt(update: Update, context: CallbackContext):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(love_strings.FLIRT_TEXT))

@run_async
def lewd(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        lewd_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(lewd_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    lewd_type = random.choice(("Text", "Gif", "Sticker"))
    if lewd_type == "Gif":
        try:
            temp = random.choice(love_strings.LEWD_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            lewd_type = "Text"

    if lewd_type == "Sticker":
        try:
            temp = random.choice(love_strings.LEWD_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            lewd_type = "Text"

    if lewd_type == "Text":
        temp = random.choice(love_strings.LEWD_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)

@run_async
def romance(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        romantic_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(romantic_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    romance_type = random.choice(("Text", "Gif", "Sticker"))
    if romance_type == "Gif":
        try:
            temp = random.choice(love_strings.ROMANCE_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            romance_type = "Text"

    if romance_type == "Sticker":
        try:
            temp = random.choice(love_strings.ROMANCE_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            romance_type = "Text"

    if romance_type == "Text":
        temp = random.choice(love_strings.ROMANCE_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)


@run_async
def owo(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        owo_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(owo_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    owo_type = random.choice(("Gif", "Sticker"))
    if owo_type == "Gif":
        try:
            temp = random.choice(love_strings.OWO_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            owo_type = "Text"

    if owo_type == "Sticker":
        try:
            temp = random.choice(love_strings.OWO_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            owo_type = "Text"


@run_async
def uwu(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        uwu_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(uwu_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    uwu_type = random.choice(("Gif", "Sticker"))
    if uwu_type == "Gif":
        try:
            temp = random.choice(love_strings.UWU_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            uwu_type = "Text"

    if uwu_type == "Sticker":
        try:
            temp = random.choice(love_strings.UWU_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            uwu_type = "Text"



__help__ = """
 • `/cuddle`*:* cuddle someone by replying to his/her message or get cuddled
 • `/hug`*:* hug someone or get hugged by Yumeko
 • `/love`*:* Checks Love in your heart weather it's true or fake
 • `/kiss`*:* Kiss someone or get kissed 
 • `/pat`*:* Pat someone or get patted by Naruto
 • `/flirt`*:* Naruto will flirt to the replied person or with you
 • `/lewd`*:* Naruto will act lewd with you or with the replied person
 • `/romance`*:* Naruto will act all romantic with you or replied person
"""

CUDDLE_HANDLER = DisableAbleCommandHandler("cuddle", cuddle)
FLIRT_HANDLER = DisableAbleCommandHandler("flirt", flirt)   
LEWD_HANDLER = DisableAbleCommandHandler("lewd", lewd) 
ROMANCE_HANDLER = DisableAbleCommandHandler("romance", romance) 
UWU_HANDLER = DisableAbleCommandHandler("uwu", uwu)
OWO_HANDLER = DisableAbleCommandHandler("owo", owo)                   

dispatcher.add_handler(CUDDLE_HANDLER)
dispatcher.add_handler(FLIRT_HANDLER)     
dispatcher.add_handler(LEWD_HANDLER)  
dispatcher.add_handler(ROMANCE_HANDLER)    
dispatcher.add_handler(UWU_HANDLER)
dispatcher.add_handler(OWO_HANDLER)                               
 
__mod_name__ = "Love"
__command_list__ = [
    "cuddle", "flirt", "lewd", "romance", "uwu", "owo"
]
__handlers__ = [
    CUDDLE_HANDLER,FLIRT_HANDLER,LEWD_HANDLER,ROMANCE_HANDLER,UWU_HANDLER,OWO_HANDLER
]
