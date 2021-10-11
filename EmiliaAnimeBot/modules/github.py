import aiohttp
from pyrogram import filters
from EmiliaAnimeBot import pgram
from EmiliaAnimeBot.pyrogramee.errors import capture_err


__mod_name__ = "Github"


@pgram.on_message(filters.command('github'))
@capture_err
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("Usage: /github username")
        return
    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'
    async with aiohttp.ClientSession() as session, session.get(URL) as request:
        if request.status == 404:
            return await message.reply_text("404")

        result = await request.json()
        try:
            url = result['html_url']
            name = result['name']
            company = result['company']
            bio = result['bio']
            created_at = result['created_at']
            avatar_url = result['avatar_url']
            blog = result['blog']
            location = result['location']
            repositories = result['public_repos']
            followers = result['followers']
            following = result['following']
            caption = f"""**Git Profile of {name}**
**Username:** `{username}`
**Bio:** `{bio}`
**Profile Link:** [Here]({url})
**Company:** `{company}`
**Created On:** `{created_at}`
**Repositories:** `{repositories}`
**Blog:** `{blog}`
**Location:** `{location}`
**Followers:** `{followers}`
**Following:** `{following}`"""
        except Exception as e:
            print(str(e))
            pass
    await message.reply_photo(photo=avatar_url, caption=caption)
