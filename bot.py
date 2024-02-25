from aiogram import Bot
from auth_data import tel_id, tokken
from bd.sqlite3 import *

chat_id = tel_id
outer_bot = Bot(tokken)


async def send_posts(post):
    for item in post:
        if not(await search_url(item[1])):
            await outer_bot.send_message(chat_id=chat_id, text=f'{item[0]}: {item[1]}')
            await add_post(item[1])


async def send_mes(mes):
    await outer_bot.send_message(chat_id=chat_id, text=mes)

