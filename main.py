#!/usr/bin/python3

from bot import send_mes, send_posts
from google import google_post
from tgstat import tg_post
from vk import vk_post
from bd.sqlite3 import *
import asyncio

async def main():
    await db_start()
    #tgp = tg_post()
    vk = vk_post()
    await send_posts(vk)
    gp = google_post()
    await send_posts(gp)
    #asyncio.run(send_mes("Отправляю пост с тг"))
    #asyncio.run(send_posts(tgp))

if __name__ == '__main__':
    asyncio.run(main())
