import aiohttp


async def fetch(url):
    async with aiohttp.ClientSession() as session, session.get(url) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data
