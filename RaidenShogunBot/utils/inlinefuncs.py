"""
Kang With Credits:

A Huge Thanks To @TheHamkerCat for this Inline Module
Make Sure to Check out!

"""

import asyncio
import os
import sys
from html import escape
from re import sub as re_sub
from sys import version as pyver
from time import ctime, time

from fuzzysearch import find_near_matches
from motor import version as mongover
from pykeyboard import InlineKeyboard
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.raw.functions import Ping
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineQueryResultArticle,
                            InlineQueryResultPhoto,
                            InputTextMessageContent)
from search_engine_parser import GoogleSearch

from EmiliaAnimeBot.extrastuff import SUDOERS
from EmiliaAnimeBot import LOG_GROUP_ID
from EmiliaAnimeBot import pgram as app 
from EmiliaAnimeBot.arqclient import arq
from EmiliaAnimeBot.utils.keyboard import ikb
from EmiliaAnimeBot.core.tasks import _get_tasks_text, all_tasks, rm_task
from EmiliaAnimeBot.core.types import InlineQueryResultCachedDocument
from EmiliaAnimeBot.modules.info import get_chat_info, get_user_info
from EmiliaAnimeBot.modules.music import download_youtube_audio
from EmiliaAnimeBot.utils.functions import test_speedtest
from EmiliaAnimeBot.utils.pastebin import paste

MESSAGE_DUMP_CHAT = LOG_GROUP_ID

meow = app.get_me()

BOT_USERNAME = meow.username
keywords_list = [
    "image",
    "wall",
    "tmdb",
    "lyrics",
    "exec",
    "speedtest",
    "search",
    "ping",
    "tr",
    "ud",
    "yt",
    "info",
    "google",
    "torrent",
    "wiki",
    "music",
    "ytmusic",
]


async def inline_help_func(__help__):
    buttons = InlineKeyboard(row_width=4)
    buttons.add(
        *[
            (
                InlineKeyboardButton(
                    text=i, switch_inline_query_current_chat=i
                )
            )
            for i in keywords_list
        ]
    )
    answerss = [
        InlineQueryResultArticle(
            title="Inline Commands",
            description="Help Related To Inline Usage.",
            input_message_content=InputTextMessageContent(
                "Click A Button To Get Started."
            ),
            thumb_url="https://hamker.me/cy00x5x.png",
            reply_markup=buttons,
        ),
        InlineQueryResultArticle(
            title="Github Repo",
            description="Get Github Respository Of Bot.",
            input_message_content=InputTextMessageContent(
                "https://github.com/IzumiCypherX/EmiliaAnimeBot"
            ),
            thumb_url="https://hamker.me/gjc9fo3.png",
        ),
    ]
    answerss = await alive_function(answerss)
    return answerss


async def alive_function(answers):
    buttons = InlineKeyboard(row_width=2)
    bot_state = "Dead" if not await app.get_me() else "Alive"
    buttons.add(
        InlineKeyboardButton("Stats", callback_data="stats_callback"),
        InlineKeyboardButton(
            "Go Inline!", switch_inline_query_current_chat=""
        ),
    )

    msg = f"""
**[Emilia✨](https://github.com/IzumiCypherX/EmiliaAnimeBot):**
**RoBot:** `{bot_state}`
**Python:** `{pyver.split()[0]}`
**Pyrogram:** `{pyrover}`
**MongoDB:** `{mongover}`
**Platform:** `{sys.platform}`
"""
    answers.append(
        InlineQueryResultArticle(
            title="Alive",
            description="Check Emilia's Stats",
            thumb_url="https://static2.aniimg.com/upload/20170515/414/c/d/7/cd7EEF.jpg",
            input_message_content=InputTextMessageContent(
                msg, disable_web_page_preview=True
            ),
            reply_markup=buttons,
        )
    )
    return answers


async def translate_func(answers, lang, tex):
    result = await arq.translate(tex, lang)
    if not result.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=result.result,
                input_message_content=InputTextMessageContent(
                    result.result
                ),
            )
        )
        return answers
    result = result.result
    msg = f"""
__**Translated from {result.src} to {result.dest}**__

**INPUT:**
{tex}

**OUTPUT:**
{result.translatedText}"""
    answers.extend(
        [
            InlineQueryResultArticle(
                title=f"Translated from {result.src} to {result.dest}.",
                description=result.translatedText,
                input_message_content=InputTextMessageContent(msg),
            ),
            InlineQueryResultArticle(
                title=result.translatedText,
                input_message_content=InputTextMessageContent(
                    result.translatedText
                ),
            ),
        ]
    )
    return answers


async def urban_func(answers, text):
    results = await arq.urbandict(text)
    if not results.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=results.result,
                input_message_content=InputTextMessageContent(
                    results.result
                ),
            )
        )
        return answers
    results = results.result[0:48]
    for i in results:
        clean = lambda x: re_sub(r"[\[\]]", "", x)
        msg = f"""
**Query:** {text}

**Definition:** __{clean(i.definition)}__

**Example:** __{clean(i.example)}__"""

        answers.append(
            InlineQueryResultArticle(
                title=i.word,
                description=clean(i.definition),
                input_message_content=InputTextMessageContent(msg),
            )
        )
    return answers


async def google_search_func(answers, text):
    gresults = await GoogleSearch().async_search(text)
    limit = 0
    for i in gresults:
        if limit > 48:
            break
        limit += 1

        try:
            msg = f"""
[{i['titles']}]({i['links']})
{i['descriptions']}"""

            answers.append(
                InlineQueryResultArticle(
                    title=i["titles"],
                    description=i["descriptions"],
                    input_message_content=InputTextMessageContent(
                        msg, disable_web_page_preview=True
                    ),
                )
            )
        except KeyError:
            pass
    return answers


async def wall_func(answers, text):
    results = await arq.wall(text)
    if not results.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=results.result,
                input_message_content=InputTextMessageContent(
                    results.result
                ),
            )
        )
        return answers
    results = results.result[0:48]
    for i in results:
        answers.append(
            InlineQueryResultPhoto(
                photo_url=i.url_image,
                thumb_url=i.url_thumb,
                caption=f"[Source]({i.url_image})",
            )
        )
    return answers


async def torrent_func(answers, text):
    results = await arq.torrent(text)
    if not results.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=results.result,
                input_message_content=InputTextMessageContent(
                    results.result
                ),
            )
        )
        return answers
    results = results.result[0:48]
    for i in results:
        title = i.name
        size = i.size
        seeds = i.seeds
        leechs = i.leechs
        upload_date = i.uploaded
        magnet = i.magnet
        caption = f"""
**Title:** __{title}__
**Size:** __{size}__
**Seeds:** __{seeds}__
**Leechs:** __{leechs}__
**Uploaded:** __{upload_date}__
**Magnet:** `{magnet}`"""

        description = f"{size} | {upload_date} | Seeds: {seeds}"
        answers.append(
            InlineQueryResultArticle(
                title=title,
                description=description,
                input_message_content=InputTextMessageContent(
                    caption, disable_web_page_preview=True
                ),
            )
        )
        pass
    return answers


async def youtube_func(answers, text):
    results = await arq.youtube(text)
    if not results.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=results.result,
                input_message_content=InputTextMessageContent(
                    results.result
                ),
            )
        )
        return answers
    results = results.result[0:48]
    for i in results:
        buttons = InlineKeyboard(row_width=1)
        video_url = f"https://youtube.com{i.url_suffix}"
        buttons.add(InlineKeyboardButton("Watch", url=video_url))
        caption = f"""
**Title:** {i.title}
**Views:** {i.views}
**Channel:** {i.channel}
**Duration:** {i.duration}
**Uploaded:** {i.publish_time}
**Description:** {i.long_desc}"""
        description = f"{i.views} | {i.channel} | {i.duration} | {i.publish_time}"
        answers.append(
            InlineQueryResultArticle(
                title=i.title,
                thumb_url=i.thumbnails[0],
                description=description,
                input_message_content=InputTextMessageContent(
                    caption, disable_web_page_preview=True
                ),
                reply_markup=buttons,
            )
        )
    return answers


async def lyrics_func(answers, text):
    song = await arq.lyrics(text)
    if not song.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=song.result,
                input_message_content=InputTextMessageContent(
                    song.result
                ),
            )
        )
        return answers
    lyrics = song.result
    song = lyrics.splitlines()
    song_name = song[0]
    artist = song[1]
    if len(lyrics) > 4095:
        lyrics = await paste(lyrics)
        lyrics = f"**Lyrics too Long:** [URL]({lyrics})"

    msg = f"__{lyrics}__"

    answers.append(
        InlineQueryResultArticle(
            title=song_name,
            description=artist,
            input_message_content=InputTextMessageContent(msg),
        )
    )
    return answers


async def tg_search_func(answers, text, user_id):
    if user_id not in SUDOERS:
        msg = "**ERROR**\n__Only For Devs__"
        answers.append(
            InlineQueryResultArticle(
                title="ERROR",
                description="Only For Devs",
                input_message_content=InputTextMessageContent(msg),
            )
        )
        return answers
    if str(text)[-1] != ":":
        msg = "**ERROR**\n__Put A ':' After The Text To Search__"
        answers.append(
            InlineQueryResultArticle(
                title="ERROR",
                description="Put A ':' After The Text To Search",
                input_message_content=InputTextMessageContent(msg),
            )
        )

        return answers
    text = text[0:-1]
    async for message in app2.search_global(text, limit=49):
        buttons = InlineKeyboard(row_width=2)
        buttons.add(
            InlineKeyboardButton(
                text="Origin",
                url=message.link
                if message.link
                else "https://t.me/telegram",
            ),
            InlineKeyboardButton(
                text="Search again",
                switch_inline_query_current_chat="search",
            ),
        )
        name = (
            message.from_user.first_name
            if message.from_user.first_name
            else "NO NAME"
        )
        caption = f"""
**Query:** {text}
**Name:** {str(name)} [`{message.from_user.id}`]
**Chat:** {str(message.chat.title)} [`{message.chat.id}`]
**Date:** {ctime(message.date)}
**Text:** >>

{message.text.markdown if message.text else message.caption if message.caption else '[NO_TEXT]'}
"""
        result = InlineQueryResultArticle(
            title=name,
            description=message.text if message.text else "[NO_TEXT]",
            reply_markup=buttons,
            input_message_content=InputTextMessageContent(
                caption, disable_web_page_preview=True
            ),
        )
        answers.append(result)
    return answers



async def wiki_func(answers, text):
    data = await arq.wiki(text)
    if not data.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=data.result,
                input_message_content=InputTextMessageContent(
                    data.result
                ),
            )
        )
        return answers
    data = data.result
    msg = f"""
**QUERY:**
{data.title}

**ANSWER:**
__{data.answer}__"""
    answers.append(
        InlineQueryResultArticle(
            title=data.title,
            description=data.answer,
            input_message_content=InputTextMessageContent(msg),
        )
    )
    return answers


async def speedtest_init(query):
    answers = []
    user_id = query.from_user.id
    if user_id not in SUDOERS:
        msg = "**ERROR**\n__THIS FEATURE IS ONLY FOR DEVS__"
        answers.append(
            InlineQueryResultArticle(
                title="ERROR",
                description="THIS FEATURE IS ONLY FOR DEVS",
                input_message_content=InputTextMessageContent(msg),
            )
        )
        return answers
    msg = "**Click The Button Below To Perform A Speedtest**"
    button = InlineKeyboard(row_width=1)
    button.add(
        InlineKeyboardButton(
            text="Start!", callback_data="test_speedtest"
        )
    )
    answers.append(
        InlineQueryResultArticle(
            title="Click Here",
            input_message_content=InputTextMessageContent(msg),
            reply_markup=button,
        )
    )
    return answers


@app.on_callback_query(filters.regex("test_speedtest"))
async def test_speedtest_cq(_, cq):
    if cq.from_user.id not in SUDOERS:
        return await cq.answer("This Isn't For You!")
    inline_message_id = cq.inline_message_id
    await app.edit_inline_text(inline_message_id, "**Testing**")
    loop = asyncio.get_running_loop()
    download, upload, info = await loop.run_in_executor(
        None, test_speedtest
    )
    msg = f"""
**Download:** `{download}`
**Upload:** `{upload}`
**Latency:** `{info['latency']} ms`
**Country:** `{info['country']} [{info['cc']}]`
**Latitude:** `{info['lat']}`
**Longitude:** `{info['lon']}`
"""
    await app.edit_inline_text(inline_message_id, msg)


async def ping_func(answers):
    ping = Ping(ping_id=app.rnd_id())
    t1 = time()
    await app.send(ping)
    t2 = time()
    ping = f"{str(round((t2 - t1) * 1000, 2))} ms"
    answers.append(
        InlineQueryResultArticle(
            title=ping,
            input_message_content=InputTextMessageContent(
                f"__**{ping}**__"
            ),
        )
    )
    return answers


async def yt_music_func(answers, url):
    if "http" not in url:
        url = (await arq.youtube(url)).result[0]
        url = f"https://youtube.com{url.url_suffix}"
    loop = asyncio.get_running_loop()
    music = await loop.run_in_executor(
        None, download_youtube_audio, url
    )
    if not music:
        msg = "**ERROR**\n__MUSIC TOO LONG__"
        answers.append(
            InlineQueryResultArticle(
                title="ERROR",
                description="MUSIC TOO LONG",
                input_message_content=InputTextMessageContent(msg),
            )
        )
        return answers
    (
        title,
        performer,
        duration,
        audio,
        thumbnail,
    ) = music
    m = await app.send_audio(
        MESSAGE_DUMP_CHAT,
        audio,
        title=title,
        duration=duration,
        performer=performer,
        thumb=thumbnail,
    )
    os.remove(audio)
    os.remove(thumbnail)
    answers.append(
        InlineQueryResultCachedDocument(
            title=title, file_id=m.audio.file_id
        )
    )
    return answers


async def info_inline_func(answers, peer):
    not_found = InlineQueryResultArticle(
        title="PEER NOT FOUND",
        input_message_content=InputTextMessageContent(
            "PEER NOT FOUND"
        ),
    )
    try:
        user = await app.get_users(peer)
        caption, _ = await get_user_info(user, True)
    except IndexError:
        try:
            chat = await app.get_chat(peer)
            caption, _ = await get_chat_info(chat, True)
        except Exception:
            return [not_found]
    except Exception:
        return [not_found]

    answers.append(
        InlineQueryResultArticle(
            title="Found Peer.",
            input_message_content=InputTextMessageContent(
                caption, disable_web_page_preview=True
            ),
        )
    )
    return answers


async def tmdb_func(answers, query):
    response = await arq.tmdb(query)
    if not response.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=response.result,
                input_message_content=InputTextMessageContent(
                    response.result
                ),
            )
        )
        return answers
    results = response.result[:49]
    for result in results:
        if not result.poster and not result.backdrop:
            continue
        if not result.genre:
            genre = None
        else:
            genre = " | ".join(result.genre)
        description = (
            result.overview[0:900] if result.overview else "None"
        )
        caption = f"""
**{result.title}**
**Type:** {result.type}
**Rating:** {result.rating}
**Genre:** {genre}
**Release Date:** {result.releaseDate}
**Description:** __{description}__
"""
        buttons = InlineKeyboard(row_width=1)
        buttons.add(
            InlineKeyboardButton(
                "Search Again",
                switch_inline_query_current_chat="tmdb",
            )
        )
        answers.append(
            InlineQueryResultPhoto(
                photo_url=result.backdrop
                if result.backdrop
                else result.poster,
                caption=caption,
                title=result.title,
                description=f"{genre} • {result.releaseDate} • {result.rating} • {description}",
                reply_markup=buttons,
            )
        )
    return answers


async def image_func(answers, query):
    results = await arq.image(query)
    if not results.ok:
        answers.append(
            InlineQueryResultArticle(
                title="Error",
                description=results.result,
                input_message_content=InputTextMessageContent(
                    results.result
                ),
            )
        )
        return answers
    results = results.result[:49]
    buttons = InlineKeyboard(row_width=2)
    buttons.add(
        InlineKeyboardButton(
            text="Search again",
            switch_inline_query_current_chat="image",
        ),
    )
    for i in results:
        answers.append(
            InlineQueryResultPhoto(
                title=i.title,
                photo_url=i.url,
                thumb_url=i.url,
                reply_markup=buttons,
            )
        )
    return answers


async def execute_code(query):
    text = query.query.strip()
    offset = int((query.offset or 0))
    answers = []
    languages = (await arq.execute()).result
    if len(text.split()) == 1:
        answers = [
            InlineQueryResultArticle(
                title=lang,
                input_message_content=InputTextMessageContent(lang),
            )
            for lang in languages
        ][offset : offset + 25]
        await query.answer(
            next_offset=str(offset + 25),
            results=answers,
            cache_time=1,
        )
    elif len(text.split()) == 2:
        text = text.split()[1].strip()
        languages = list(
            filter(
                lambda x: find_near_matches(text, x, max_l_dist=1),
                languages,
            )
        )
        answers.extend(
            [
                InlineQueryResultArticle(
                    title=lang,
                    input_message_content=InputTextMessageContent(
                        lang
                    ),
                )
                for lang in languages
            ][:49]
        )
    else:
        lang = text.split()[1]
        code = text.split(None, 2)[2]
        response = await arq.execute(lang, code)
        if not response.ok:
            answers.append(
                InlineQueryResultArticle(
                    title="Error",
                    input_message_content=InputTextMessageContent(
                        response.result
                    ),
                )
            )
        else:
            res = response.result
            stdout, stderr = escape(res.stdout), escape(res.stderr)
            output = stdout or stderr
            out = (
                "STDOUT"
                if stdout
                else ("STDERR" if stderr else "No output")
            )

            msg = f"""
**{lang.capitalize()}:**
```{code}```

**{out}:**
```{output}```
            """
            answers.append(
                InlineQueryResultArticle(
                    title="Executed",
                    description=output[:20],
                    input_message_content=InputTextMessageContent(
                        msg
                    ),
                )
            )
    await query.answer(results=answers, cache_time=1)


async def task_inline_func(user_id):
    if user_id not in SUDOERS:
        return

    tasks = all_tasks()
    text = await _get_tasks_text()
    keyb = None

    if tasks:
        keyb = ikb(
            {i: f"cancel_task_{i}" for i in list(tasks.keys())},
            row_width=4,
        )

    return [
        InlineQueryResultArticle(
            title="Tasks",
            reply_markup=keyb,
            input_message_content=InputTextMessageContent(
                text,
            ),
        )
    ]


@app.on_callback_query(filters.regex("^cancel_task_"))
async def cancel_task_button(_, query: CallbackQuery):
    user_id = query.from_user.id

    if user_id not in SUDOERS:
        return await query.answer("This is not for you.")

    task_id = int(query.data.split("_")[-1])
    await rm_task(task_id)

    tasks = all_tasks()
    text = await _get_tasks_text()
    keyb = None

    if tasks:
        keyb = ikb(
            {i: f"cancel_task_{i}" for i in list(tasks.keys())}
        )

    await app.edit_inline_text(
        query.inline_message_id,
        text,
    )

    if keyb:
        await app.edit_inline_reply_markup(
            query.inline_message_id,
            keyb,
        )
