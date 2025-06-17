from aiogram import Bot, Dispatcher, executor
import asyncio
import time
from aiogram import types
from datetime import datetime

import handlers
import gettime
import get_comm
import bd
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

bd.chats_create()
bd.db_user_create()
bd.db_user_chat_connect_create()

dp.register_message_handler(handlers.help, commands=["help"])
dp.register_message_handler(get_comm.get_com, content_types=['photo'], commands=["sosal"])
dp.register_message_handler(get_comm.get_comSOS, commands=["sosal"])
dp.register_message_handler(get_comm.check_sos, commands=["now"])

user_list = []

@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 
                           '@all Готовы сосать, господа? ')
    global time_sos
    time_sos = gettime.get_time()
    bd.write_chat(time_sos, chat_id)
    while True:
        await asyncio.sleep(5)
        now = datetime.now()
        current_time = now.strftime("%d-%H-%M")
        time_sos = bd.get_time(chat_id)
        if current_time == time_sos: 
            global user_list
            user_list = bd.get_users(message.chat.id)
            time_sos = gettime.get_time()
            bd.write_time(time_sos, chat_id)
            await bot.send_message(chat_id, 
                                   '@all Время сосать, господа!!! ') 
            
    
            
@dp.message_handler(commands=['check'])
async def check(message: types.Message):
    chat_id = message.chat.id
    t = bd.get_time(chat_id)
    await message.answer(f" Время следующего сосания: " + t)

@dp.message_handler(commands=['now_check'])
async def check1(message: types.Message):
    chat_id = message.chat.id  # Получаем ID чата
    new_time_sos = datetime.now().strftime("%d-%H-%M")  # Записываем текущее время
    bd.write_time(new_time_sos, chat_id)  # Записываем время в базу данных
    await message.answer("Время обновлено!")

"""@dp.message_handler(commands=['now_check'])
async def check1(message: types.Message):
    global time_sos
    time_sos = datetime.now().strftime("%d-%H-%M")"""

@dp.message_handler(commands=['get_user'])
async def check2(message: types.Message):
    global user_list
    await message.answer(user_list)

@dp.message_handler(content_types=types.ContentType.PHOTO)  
async def echo_message(message: types.Message):
    global user_list
    if message.from_user.id in user_list:
        user_list.pop(user_list.index(message.from_user.id))
        await message.reply(f"Спасибо дорогой!")
        await message.answer(get_comm.get_com_choice())

@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo_message(message: types.Message):
    global user_list
    if message.from_user.id in user_list:
        await message.reply(f"Скинь фото, олух")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
