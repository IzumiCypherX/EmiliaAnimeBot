from EmiliaAnimeBot import dispatcher

from telegram import ParseMode, Update, CallbackContext
from telegram.ext import CommandHandler, run_aysnc

GIT_PIC = "https://telegra.ph/file/311df2003dc985a39ddf6.jpg"

GIT_TEXT = """
EmiliaAnimeRobot By @TheSidharthaRao

*Contributors/Credits*

> [IzumiCypherX](https://github.com/IzumiCypherX)
> [Nautilus](https://github.com/sudo-nautilus)
> [Kaneki](https://github.com/KanekiKen44)
> [Paul-Larsen](https://github.com/PaulSonofLars)
> [TheHamkerCat](https://github.com/TheHamkerCat)


[Repository](https://github.com/IzumiCypherX/EmiliaAnimeBot)
[Support](https://telegram.dog/TangentChats)
[Docs](https://telegra.ph/file/dc836cb6f93a6e91dfa68.jpg)

"""

@run_async
def repo(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(
        GIT_PIC,
        caption = GIT_TEXT,
        parse_mode=ParseMode.MARKDOWN
        )

REPO_HANDLER = CommandHandler("repo", repo)

disaptcher.add_handler(REPO_HANDLER)
