import asyncio
from asyncio import sleep

from telethon import events
from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins

from SaitamaRobot import telethn, OWNER_ID, DEV_USERS, DRAGONS, TIGERS

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)


UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

GHOSTHUNTERS = [OWNER_ID] + DEV_USERS + DRAGONS + TIGERS

async def is_administrator(user_id: int, message):
    admin = False
    async for user in telethn.iter_participants(
        message.chat_id, filter=ChannelParticipantsAdmins
    ):
        if user_id == user.id or user_id in GHOSTHUNTERS:
            admin = True
            break
    return admin



@telethn.on(events.NewMessage(pattern=f"^[!/]ghosts ?(.*)"))
async def ghosts(event):
    """ For /ghosts command, list all the  in a chat. """

    con = event.pattern_match.group(1).lower()
    del_u = 0
    del_status = "No Deleted Accounts Found, Group Is Clean."

    if con != "clean":
        find_ghosts = await event.respond("Searching For Ghosts...")
        async for user in event.client.iter_participants(event.chat_id):

            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = f"Found **{del_u}** ghosts In This Group.\
            \nClean Them By Using :-\n 👉 `/ghosts clean`"
        await find_ghosts.edit(del_status)
        return

    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    
    if not await is_administrator(user_id=event.from_id, message=event):
        await event.respond("You're Not An Admin!")
        return
    
    if not admin and not creator:
        await event.respond("I Am Not An Admin Here!")
        return

    cleaning_ghosts = await event.respond("Cleaning ghosts...")
    del_u = 0
    del_a = 0

    async for user in event.client.iter_participants(event.chat_id):
        if user.deleted:
            try:
                await event.client(
                    EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                await cleaning_ghosts.edit("I Don't Have Ban Rights In This Group.")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        del_status = f"Cleaned `{del_u}` ghosts"

    if del_a > 0:
        del_status = f"Cleaned `{del_u}` ghosts \
        \n`{del_a}` Zombie Admin Accounts Are Not Removed!"

    await cleaning_ghosts.edit(del_status)