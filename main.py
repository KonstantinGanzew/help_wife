from bot import send_mes, send_posts
from google import google_post
from tgstat import tg_post
from vk import vk_post
import asyncio

def main():
    #gp = google_post()
    #tgp = tg_post()
    vk = vk_post()
    gp = google_post()
    print(type(vk))
    #asyncio.run(send_mes("Отправляю пост с вк"))
    asyncio.run(send_posts(vk))
    #asyncio.run(send_mes("Отправляю пост с гугла"))
    asyncio.run(send_posts(gp))
    #asyncio.run(send_mes("Отправляю пост с тг"))
    #asyncio.run(send_posts(tgp))
    
if __name__ == '__main__':
    main()