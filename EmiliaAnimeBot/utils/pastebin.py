from EmiliaAnimeBot.utils.http import post

BASE = "https://batbin.me/"


async def paste(content: str):
    resp = await post(f"{BASE}api/paste", data={"content": content})
    if not resp["status"]:
        return
    return BASE + resp["message"]