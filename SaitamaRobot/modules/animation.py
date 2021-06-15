import time

from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot.modules.helper_funcs.chat_status import user_admin
from telegram import Update
from telegram.ext import CallbackContext, run_async

#sleep how many times after each edit in 'onichan'
EDIT_SLEEP = 2
#edit how many times in 'onichan'
EDIT_TIMES = 5

EDIT_TIMES_KILL = 2

POLICE_SIREN = [
    "🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵",
    "🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴"
]

LOVE_EMOJY = [
    "❤️🧡❤️💚❤️💙❤️💜\n❤️💜❤️💙❤️💚❤️🧡\n❤️🧡❤️💚❤️💙❤️💜",
    "💜❤️💜💙💜💚💜🧡\n🧡❤️💚❤️💙❤️💜❤️\n💜❤️💙❤️💚❤️🧡❤️"
]

KILL_STRING = [
    "Pathetic Human Die👿!\n\n(　･ิω･ิ)︻デ═一-->\n\n------>\n\n----------->",
    "---->\n\n(￣ー￣) DEAD😈😈\n\n\nUwU user killed successful!\n\n*happy noises😈😈*"
]

@user_admin
@run_async
def onichan(update: Update, context: CallbackContext):
    msg = update.effective_message.reply_text('onichan onichan police is coming!')
    for x in range(EDIT_TIMES):
        msg.edit_text(POLICE_SIREN[x % 2])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('onichan , you are under arrest!')

@run_async
def love(update: Update, context: CallbackContext):
    msg = update.effective_message.reply_text('checking love')
    for x in range(EDIT_TIMES):
        msg.edit_text(LOVE_EMOJY[x % 2])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('True Love!')

@run_async
def kill(update: Update, context: CallbackContext):
    msg = update.effective_message.reply_text('getting my gun👿👿.')
    for x in range(EDIT_TIMES_KILL):
        msg.edit_text(KILL_STRING[x % 2])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('UwU Target killed successfully😈!\n\n\n*Happy noises😈😈*')

__help__ = """
• `/onichan`*:* Sends a police to arrest your onichan. 
• `/kill`*:* Kills the targeted person with a animated gun.
"""

ONICHAN_HANDLER = DisableAbleCommandHandler("onichan", onichan)
LOVE_HANDLER = DisableAbleCommandHandler("love", love)
KILL_HANDLER = DisableAbleCommandHandler ("kill", kill)
dispatcher.add_handler(ONICHAN_HANDLER)
dispatcher.add_handler(LOVE_HANDLER)
dispatcher.add_handler(KILL_HANDLER)

__mod_name__ = "Animation"
__command_list__ = ["onichan", "love", "kill"]
__handlers__ = [ONICHAN_HANDLER , LOVE_HANDLER , KILL_HANDLER]
