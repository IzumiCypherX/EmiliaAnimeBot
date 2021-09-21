import html

from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import mention_html

from RaidenShogunBot import (DEV_USERS, LOGGER, OWNER_ID, DRAGONS, DEMONS, TIGERS,
                          WOLVES, dispatcher)
from RaidenShogunBot.modules.disable import DisableAbleCommandHandler
from RaidenShogunBot.modules.helper_funcs.chat_status import (
    bot_admin, can_restrict, connection_status, is_user_admin,
    is_user_ban_protected, is_user_in_chat, user_admin, user_can_ban)
from RaidenShogunBot.modules.helper_funcs.extraction import extract_user_and_text
from RaidenShogunBot.modules.helper_funcs.string_handling import extract_time
from RaidenShogunBot.modules.log_channel import gloggable, loggable

@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def ban(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    log_message = ""
    bot = context.bot
    args = context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("My Sixth Sense says this is not a User.")
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message == "User not found":
            message.reply_text("Can't seem to find this person.")
            return log_message
        else:
            raise

    if user_id == bot.id:
        message.reply_text("Oh yeah, ban myself, Baka!")
        return log_message

    if is_user_ban_protected(chat, user_id, member) and user not in DEV_USERS:
        if user_id == OWNER_ID:
            message.reply_text(
                "Trying to put me against the God of Chakra huh?")
            return log_message
        elif user_id in DEV_USERS:
            message.reply_text("I can't act against our own.")
            return log_message
        elif user_id in DRAGONS:
            message.reply_text(
                "I won't want to fight this Shinobi without Higher permission.")
            return log_message
        elif user_id in DEMONS:
            message.reply_text(
                "Bring an order from Gods to fight this Shinobi."
            )
            return log_message
        elif user_id in TIGERS:
            message.reply_text(
                "Bring an order from Gods to fight a respected Shinobi."
            )
            return log_message
        elif user_id in WOLVES:
            message.reply_text("Abilities of this Shinobi makes them ban immune!")
            return log_message
        else:
            message.reply_text("This user has immunity and cannot be banned.")
            return log_message

    log = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#BANNED\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
    )
    if reason:
        log += "\n<b>Reason:</b> {}".format(reason)

    try:
        chat.kick_member(user_id)
        # bot.send_sticker(chat.id, BAN_STICKER)  # banhammer marie sticker
        reply = (
            f"<code>⛔</code><b>Ban Event</b>\n"
            f"<code> </code><b>•  User:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
        )
        if reason:
            reply += f"\n<code> </code><b>•  Reason:</b> \n{html.escape(reason)}"
        bot.sendMessage(chat.id, reply, parse_mode=ParseMode.HTML, quote=False)
        return log

    except BadRequest as excp:
        if excp.message == "Reply message not found":
            # Do not reply
            message.reply_text('Banned!', quote=False)
            return log
        else:
            LOGGER.warning(update)
            LOGGER.exception("ERROR banning user %s in chat %s (%s) due to %s",
                             user_id, chat.title, chat.id, excp.message)
            message.reply_text("Uhm...that didn't work...")

    return log_message


  
@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def sban(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    log_message = ""
    bot = context.bot
    args = context.args
    user_id, reason = extract_user_and_text(message, args)
    update.effective_message.delete()
    if not user_id:
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message == "User not found":
            return log_message
        else:
            raise

    if user_id == bot.id:
        return log_message

    if is_user_ban_protected(chat, user_id, member):
        return log_message
      
    if user_id == 777000 or user_id == 1087968824:
        return log_message
      
    log = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#SBANNED\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
    )
    if reason:
        log += "\n<b>Reason:</b> {}".format(reason)

    try:
        chat.kick_member(user_id)
        return log

    except BadRequest as excp:
        if excp.message == "Reply message not found":
            return log
        else:
            LOGGER.warning(update)
            LOGGER.exception("ERROR banning user %s in chat %s (%s) due to %s",
                             user_id, chat.title, chat.id, excp.message)
    return log_message


@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def temp_ban(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    log_message = ""
    bot, args = context.bot, context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("I doubt that's a user.")
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message == "User not found":
            message.reply_text("I can't seem to find this user.")
            return log_message
        else:
            raise

    if user_id == bot.id:
        message.reply_text("I'm not gonna BAN myself, are you crazy?")
        return log_message

    if is_user_ban_protected(chat, user_id, member):
        message.reply_text("I don't feel like I can Ban This User")
        return log_message

    if not reason:
        message.reply_text("You haven't specified a time to ban this user for!")
        return log_message

    split_reason = reason.split(None, 1)

    time_val = split_reason[0].lower()
    if len(split_reason) > 1:
        reason = split_reason[1]
    else:
        reason = ""

    bantime = extract_time(message, time_val)

    if not bantime:
        return log_message

    log = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        "#TEMP BANNED\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}\n"
        f"<b>Time:</b> {time_val}")
    if reason:
        log += "\n<b>Reason:</b> {}".format(reason)

    try:
        chat.kick_member(user_id, until_date=bantime)
        # bot.send_sticker(chat.id, BAN_STICKER)  # banhammer marie sticker
        bot.sendMessage(
            chat.id,
            f"Banned! User {mention_html(member.user.id, html.escape(member.user.first_name))} "
            f"will be banned for {time_val}.",
            parse_mode=ParseMode.HTML)
        return log

    except BadRequest as excp:
        if excp.message == "Reply message not found":
            # Do not reply
            message.reply_text(
                f"Banned! User will be banned for {time_val}.", quote=False)
            return log
        else:
            LOGGER.warning(update)
            LOGGER.exception("ERROR banning user %s in chat %s (%s) due to %s",
                             user_id, chat.title, chat.id, excp.message)
            message.reply_text("Well damn, I can't ban that user.")

    return log_message

  
@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def stemp_ban(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    log_message = ""
    bot, args = context.bot, context.args
    user_id, reason = extract_user_and_text(message, args)
    update.effective_message.delete()
    if not user_id:
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message == "User not found":
            return log_message
        else:
            raise

    if user_id == bot.id:
        return log_message

    if is_user_ban_protected(chat, user_id, member):
        return log_message

    if not reason:
        message.reply_text("You haven't specified a time to ban this user for!")
        return log_message

    split_reason = reason.split(None, 1)

    time_val = split_reason[0].lower()
    if len(split_reason) > 1:
        reason = split_reason[1]
    else:
        reason = ""

    bantime = extract_time(message, time_val)

    if not bantime:
        return log_message

    log = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        "#STEMP BANNED\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}\n"
        f"<b>Time:</b> {time_val}")
    if reason:
        log += "\n<b>Reason:</b> {}".format(reason)

    try:
        chat.kick_member(user_id, until_date=bantime)
        # bot.send_sticker(chat.id, BAN_STICKER)  # banhammer marie sticker
        return log

    except BadRequest as excp:
        if excp.message == "Reply message not found":
            # Do not reply
            return log
        else:
            LOGGER.warning(update)
            LOGGER.exception("ERROR banning user %s in chat %s (%s) due to %s",
                             user_id, chat.title, chat.id, excp.message)
    return log_message

  
@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def kick(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    log_message = ""
    bot, args = context.bot, context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("Error While Getiing the User ID")
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message == "User not found":
            message.reply_text("I can't seem to find this user.")
            return log_message
        else:
            raise

    if user_id == bot.id:
        message.reply_text("I've been taught: Never Hurt Yourself")
        return log_message

    if is_user_ban_protected(chat, user_id):
        message.reply_text("The User is Ban-Protected smh..")
        return log_message

    res = chat.unban_member(user_id)  # unban on current user = kick
    if res:

        bot.sendMessage(
            chat.id,
            f"User Kicked Woops! {mention_html(member.user.id, html.escape(member.user.first_name))}.",
            parse_mode=ParseMode.HTML)
        log = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"#KICKED\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
        )
        if reason:
            log += f"\n<b>Reason:</b> {reason}"

        return log

    else:
        message.reply_text("Well damn, I can't kick that user.")

    return log_message


@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def skick(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    log_message = ""
    bot, args = context.bot, context.args
    user_id, reason = extract_user_and_text(message, args)
    update.effective_message.delete()
    if not user_id:
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message == "User not found":
            return log_message
        else:
            raise

    if user_id == bot.id:
        return log_message

    if is_user_ban_protected(chat, user_id):
        return log_message

    res = chat.unban_member(user_id)  # unban on current user = kick
    if res:
        log = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"#SKICKED\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
        )
        if reason:
            log += f"\n<b>Reason:</b> {reason}"

        return log

    return log_message
  
  
@run_async
@bot_admin
@can_restrict
def kickme(update: Update, context: CallbackContext):
    user_id = update.effective_message.from_user.id
    if is_user_admin(update.effective_chat, user_id):
        update.effective_message.reply_text(
            "Surrender your adminship and try again!")
        return

    res = update.effective_chat.unban_member(
        user_id)  # unban on current user = kick
    if res:
        update.effective_message.reply_text("Ara Ara! Sayonara!")
    else:
        update.effective_message.reply_text("The Holy Scriptures make me refrain from doing so...")


@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def unban(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    log_message = ""
    bot, args = context.bot, context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("I doubt that's a user.")
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message == "User not found":
            message.reply_text("I can't seem to find this user.")
            return log_message
        else:
            raise

    if user_id == bot.id:
        message.reply_text("How would I unban myself if I wasn't here...?")
        return log_message

    if is_user_in_chat(chat, user_id):
        message.reply_text("Isn't this person already here??")
        return log_message

    chat.unban_member(user_id)
    message.reply_text("Yep, this user can join!")

    log = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#UNBANNED\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
    )
    if reason:
        log += f"\n<b>Reason:</b> {reason}"

    return log


@run_async
@connection_status
@bot_admin
@can_restrict
@gloggable
def selfunban(context: CallbackContext, update: Update) -> str:
    message = update.effective_message
    user = update.effective_user
    bot, args = context.bot, context.args
    if user.id not in DRAGONS or user.id not in TIGERS:
        return

    try:
        chat_id = int(args[0])
    except:
        message.reply_text("Give a valid chat ID.")
        return

    chat = bot.getChat(chat_id)

    try:
        member = chat.get_member(user.id)
    except BadRequest as excp:
        if excp.message == "User not found":
            message.reply_text("I can't seem to find this user.")
            return
        else:
            raise

    if is_user_in_chat(chat, user.id):
        message.reply_text("Aren't you already in the chat??")
        return

    chat.unban_member(user.id)
    message.reply_text("Yep, I have unbanned you.")

    log = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#UNBANNED\n"
        f"<b>User:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
    )

    return log


__help__ = """
*Kicks:*
 - `/kick <userhandle>`*:* Kicks a user out of the group, (via handle, or reply)
 - `/skick <userhandle>`*:* Silently kicks a user out of the group, (via handle, or reply)
 - `/kickme`*:* Kicks the user who used the command.
 
*Bans:*
 - `/ban <userhandle>`*:* Bans a user. (via handle, or reply)
 - `/sban <userhandle>`*:* Silently bans a user without leaving any message. (via handle, or reply)
 - `/tban <userhandle> x(m/h/d)`*:* Bans a user for `x` time. (via handle, or reply). `m` = `minutes`, `h` = `hours`, `d` = `days`.
 - `/stban <userhandle> x(m/h/d)`*:* Silently bans a user for `x` time. (via handle, or reply). `m` = `minutes`, `h` = `hours`, `d` = `days`.
 - `/unban <userhandle>`*:* Unbans a user. (via handle, or reply)

_NOTE:_
 If you set Log Channels, you will get logs of Silent kick and bans. Check *Logger* module to know more about Log Channel.
"""

BAN_HANDLER = CommandHandler("ban", ban)
TEMPBAN_HANDLER = CommandHandler(["tban"], temp_ban)
STEMPBAN_HANDLER = CommandHandler(["stban"], stemp_ban)
KICK_HANDLER = CommandHandler("kick", kick)
SKICK_HANDLER = CommandHandler("skick", skick)
UNBAN_HANDLER = CommandHandler("unban", unban)
ROAR_HANDLER = CommandHandler("roar", selfunban)
KICKME_HANDLER = DisableAbleCommandHandler(
    "kickme", kickme, filters=Filters.group)
SBAN_HANDLER = CommandHandler("sban", sban)

dispatcher.add_handler(BAN_HANDLER)
dispatcher.add_handler(TEMPBAN_HANDLER)
dispatcher.add_handler(STEMPBAN_HANDLER)
dispatcher.add_handler(KICK_HANDLER)
dispatcher.add_handler(SKICK_HANDLER)
dispatcher.add_handler(UNBAN_HANDLER)
dispatcher.add_handler(ROAR_HANDLER)
dispatcher.add_handler(KICKME_HANDLER)
dispatcher.add_handler(SBAN_HANDLER)

__mod_name__ = "Bans"
__handlers__ = [
    BAN_HANDLER, TEMPBAN_HANDLER, STEMPBAN_HANDLER, KICK_HANDLER, SKICK_HANDLER, UNBAN_HANDLER, ROAR_HANDLER,
    KICKME_HANDLER, SBAN_HANDLER
]
