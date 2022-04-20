from pyrogram import Client
from pyrogram import filters
from pyrogram import types
import sqlite3
import time
import random
import asyncio
app = Client('my_accounts')

my_id = 1045832338
id_chat= '-1001725761556'
voice_chat_id = -1001533221887

session_ids = [2138114850,2117293568,2109691120,
2111537384,2140054039,2143075798,
2104949535,2126724940,2121285225,
2133079225,2126250972,2115575454,
2102982104,2095771800,2118144794,
2104334929,2120884883,2143437907]

@app.on_message(filters.me)
async def payments (client,message):
    print(message)
    global id_chat
    if message.from_user.id == my_id and message.text == 'Аа':
                await app.edit_message_text(message_id=message.message_id,chat_id=message.chat.id,text="""Реквизиты для оплаты спр>
                🇰🇬Mbank online - <pre>996772187870</pre>
🇰🇬Элсом - <pre>0770350099</pre>
🇺🇿Uzcard - <pre>8600120420267414</pre>
🇰🇿Каспи - <pre>77782085140</pre>
▫️Киви - <pre>79183561047</pre>
▫️Юмани  - <pre>410019301888334</pre>
<b>Стоимость - 5.88$</b>
🇰🇬 473 сом
🇺🇿 66 440 сум 
🇰🇿 2 671 тенге
Курс если изменился, не проблема😉 меняй)) 
Если с другой страны, напиши с какой  решим)
Как оплатишь, чек, или скрин оплаты отправь мне 😎 
После добавлю тебя в спринт⚡""",parse_mode='html')

        await app.copy_message(chat_id=message.chat.id,from_chat_id=voice_chat_id,message_id=19)


    if message.from_user.id == my_id and message.text == 'Пппп':
        await app.delete_messages(chat_id=message.chat.id,message_ids=message.message_id)
        id_user = message.chat.id
        try:
            await app.add_chat_members(chat_id=id_chat,user_ids=id_user)
            await app.send_message(chat_id=message.chat.id, text="""Еее 🥳🥳 всё, добавил тебя в спринт, 
Глянь чат, там тебе прислали обучение 👇""")
        except:
            await app.send_message(chat_id=message.chat.id, text="""Не могу добавить, так как тебя запрещено приглашать в беседы.

Что бы это исправить переходи в настройки телеграма:

- Конфидециальность
- Группы и каналы
И добавь меня в список тех, кто тебя может приглашать в группы и каналы)
Либо, открой доступ для всех, так
быстрей 😅

После этого напиши мне, и мы повторим попытку😎""")
        await app.copy_message(chat_id=message.chat.id, from_chat_id=voice_chat_id,message_id=17)


    if message.from_user.id == my_id and message.text == 'Вввв':
        await app.delete_messages(chat_id=message.chat.id, message_ids=message.message_id)
        await app.copy_message(chat_id=message.chat.id, from_chat_id=voice_chat_id, message_id=13)

    if message.from_user.id == my_id and message.text == 'Сделать группу основной':
        id_chat = (message.chat.id)
        for id in session_ids:
            try:
                await app.get_chat_member(chat_id=id_chat,user_id=id)

            except: #Если ошибка - добавляем чела в чат
                try:
                    await app.add_chat_members(chat_id=id_chat, user_ids=id)
                    await asyncio.sleep(1)
                except:
                    pass



app.run()
