import asyncio
import traceback

from pyrogram import filters
from pyrogram.types import ChatPermissions
from KURUMIBOT import OWNER_ID
import os 


from KURUMIBOT import BOT_ID, DRAGONS
from KURUMIBOT import pbot as app
from KURUMIBOT import pbot


async def member_permissions(chat_id: int, user_id: int):
    perms = []
    member = await app.get_chat_member(chat_id, user_id)
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    if member.can_manage_voice_chats:
        perms.append("can_manage_voice_chats")
    return perms


async def current_chat_permissions(chat_id):
    perms = []
    perm = (await app.get_chat(chat_id)).permissions
    if perm.can_send_messages:
        perms.append("can_send_messages")
    if perm.can_send_media_messages:
        perms.append("can_send_media_messages")
    if perm.can_send_stickers:
        perms.append("can_send_stickers")
    if perm.can_send_animations:
        perms.append("can_send_animations")
    if perm.can_send_games:
        perms.append("can_send_games")
    if perm.can_use_inline_bots:
        perms.append("can_use_inline_bots")
    if perm.can_add_web_page_previews:
        perms.append("can_add_web_page_previews")
    if perm.can_send_polls:
        perms.append("can_send_polls")
    if perm.can_change_info:
        perms.append("can_change_info")
    if perm.can_invite_users:
        perms.append("can_invite_users")
    if perm.can_pin_messages:
        perms.append("can_pin_messages")

    return perms


# Purge Messages



@pbot.on_message(filters.command("spurge"))
async def purge(client, message):
    try:
        message_ids = []
        chat_id = message.chat.id
        user_id = message.from_user.id
        if message.chat.type not in ("supergroup", "channel"):
            return
        permissions = await member_permissions(chat_id, user_id)
        if "can_delete_messages" in permissions or user_id in DRAGONS:
            if message.reply_to_message:
                for a_s_message_id in range(
                    message.reply_to_message.message_id, message.message_id
                ):
                    message_ids.append(a_s_message_id)
                    if len(message_ids) == 100:
                        await client.delete_messages(
                            chat_id=chat_id,
                            message_ids=message_ids,
                            revoke=True,
                        )
                        message_ids = []
                if len(message_ids) > 0:
                    await client.delete_messages(
                        chat_id=chat_id, message_ids=message_ids, revoke=True
                    )
            else:
                await message.reply_text(
                    "Reply To A Message To Delete It,"
                    " Don't Make Fun Of Yourself!"
                )
        else:
            await message.reply_text("Your Don't Have Enough Permissions!")
        await message.delete()
    except Exception as e:
        await message.reply_text(str(e))
        e = traceback.format_exc()
        print(e)


@pbot.on_message(filters.command("fullpromote"))
async def promote(_, message):
    try:
        from_user_id = message.from_user.id
        chat_id = message.chat.id
        permissions = await member_permissions(chat_id, from_user_id)
        if (
            "can_promote_members" not in permissions
            and from_user_id not in DRAGONS
        ):
            await message.reply_text("You don't have enough permissions")
            return
        bot = await app.get_chat_member(chat_id, BOT_ID)
        if len(message.command) == 2:
            username = message.text.split(None, 1)[1]
            user_id = (await app.get_users(username)).id
        elif len(message.command) == 1 and message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        else:
            await message.reply_text(
                "Reply To A User's Message Or Give A Username To Promote."
            )
            return
        await message.chat.promote_member(
            user_id=user_id,
            can_change_info=bot.can_change_info,
            can_invite_users=bot.can_invite_users,
            can_delete_messages=bot.can_delete_messages,
            can_restrict_members=True,
            can_pin_messages=bot.can_pin_messages,
            can_promote_members=bot.can_promote_members,
            can_manage_chat=bot.can_manage_chat,
            can_manage_voice_chats=bot.can_manage_voice_chats,
        )
        await message.reply_text("Sucessfully Full Promoted this user!")

    except Exception as e:
        await message.reply_text(str(e))
        e = traceback.format_exc()
        print(e)
