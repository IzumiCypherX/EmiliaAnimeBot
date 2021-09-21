
"""
import codecs
import pickle
from typing import Dict, List, Union

from EmiliaAnimeBot.mongo import db



async def user_global_karma(user_id) -> int:
    chats = karmadb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return 0
    total_karma = 0
    for chat in await chats.to_list(length=1000000):
        karma = await get_karma(
            chat["chat_id"], await int_to_alpha(user_id)
        )
        if karma and (int(karma["karma"]) > 0):
            total_karma += int(karma["karma"])
    return total_karma

async def is_gbanned_user(user_id: int) -> bool:
    user = await gbansdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True
"""
