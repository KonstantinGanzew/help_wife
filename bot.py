from aiogram import Bot
from auth_data import tel_id, tokken
import time
import asyncio

chat_id = tel_id
outer_bot = Bot(tokken)


async def send_posts(post):
    for item in post:
        await outer_bot.send_message(chat_id=chat_id, text=f'{item[0]}: {item[1]}')

async def send_mes(mes):
    await outer_bot.send_message(chat_id=chat_id, text=mes)


#test = [['Депутат Госдумы Александр Хинштейн отреагировал на оправдания топ-менеджеров телеком-оператора «Уфанет» по поводу того, что компания находится под...', 'https://telesputnik.ru/materials/hipe/news/hinshteyn-vozmutilsya-opravdaniyami-ufanet-po-povodu-inostrannyh-vladelcev'], ['Депутат Госдумы Александр Хинштейн выступил с заявлением о том, что совладелец "Уфанета" распространяет фейки об СВО.', 'https://ufa-town.ru/news/view/deputat-gosdumy-hinstejn-sovladelec-ufaneta-rasprostranaet-fejki-ob-svo'], ['Заявление депутата Госдумы Александра Хинштейна об изъятии активов у директоров «Уфанета» удивило многих. Особенно щедрыми - Политика - 21 февраля 2024...', 'https://ufa1.ru/text/politics/2024/02/21/73252889/'], ['Серьезнейший процесс передела собственности стартовал на телекоммуникационном рынке Башкортостана. Крупнейший местный провайдер «Уфанет»,...', 'https://pravdapfo.ru/polnotekst/475421-ufanet-gotovitsya-povtorit-sudbu-bashsody-iz-za-poziczii-i-grazhdanstva-uchreditelej/'], ['Депутат Госдумы Александр Хинштейн считает, что телеком-оператор из Башкирии «Уфанет» попадает под закон, позволяющий конфисковывать - Политика - 20 февраля...', 'https://ufa1.ru/text/politics/2024/02/20/73250504/'], ['Хинштейн заявил, что предприниматель Марат Ахметшин — не просто «уфимский бизнесмен», а совладелец телеком-оператора “Уфанет”.', 'https://www.business-gazeta.ru/news/623828'], ['В Госдуме предложили изъять акции «Уфанета», которые принадлежат бизнесменам Марату Ахметшину и Марату Фаттахову. С такой идеей выступил деп...', 'https://ufatime.ru/news/2024/02/20/v-gosdume-predlozhili-konfiskovat-chast-akcij-ufaneta/'], ['Депутат Госдумы Александр Хинштейн призвал вывести компанию «Уфанет» из-под иностранного контроля. Он сообщил, что 29,9% акций компании принадлежат...', 'https://ufa-town.ru/news/view/hinstejn-prizval-vyvesti-ufanet-iz-pod-inostrannogo-kontrola'], ['На днях совладелец Уфанет сделал громкое заявление на своей странице в соц сетях. Высказывание не осталось незамеченным и быстро последовала реплика...', 'https://telecomtimes.ru/2024/02/ufanet/'], ['Депутат Госдумы Александр Хинштейн призвал конфисковать акции компании «Уфанет» у совладельца телеком-оператора Марата Ахметшина и его партнера Марата...', 'https://telesputnik.ru/materials/novosti-kompanii/news/hinshteyn-prizval-vyvesti-iz-pod-inostrannogo-kontrolya-operatora-ufanet']]

#asyncio.run(send_posts(test))