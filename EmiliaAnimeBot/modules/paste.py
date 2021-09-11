import requests
from EmiliaAnimeBot import dispatcher
from EmiliaAnimeBot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async


PASTED_IMG = "https://telegra.ph/file/94ab47d1fb4c2c3dc9109.jpg"


@run_async
def paste(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message

    if message.reply_to_message:
        txt = message.reply_to_message.text

    elif len(args) >= 1:
        txt = message.text.split(None, 1)[1]

    else:
        message.reply_text("What am I supposed to do with this?")
        return

    npaste = requests.post(post, data={"content": txt})
   
    url = f'www.nekobin.com/{npaste.json()['result']['key']}'

    reply_text = f'Pasted to NekoBin!'


    message.reply_photo(
        PASTED_IMG, caption=reply_text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup = InlineKeyboardMarkup(
            [
                InlineKeyboardButton(text="Link", url={url})
            ]
        )
        )


PASTE_HANDLER = DisableAbleCommandHandler("paste", paste)
dispatcher.add_handler(PASTE_HANDLER)

__command_list__ = ["paste"]
__handlers__ = [PASTE_HANDLER]
