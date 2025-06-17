import random as rd
import neuro
import bd
from aiogram import types

f = open("C:/My/SosaBot/myBot/commentSos.txt", "+r", encoding="utf-8")
comment = f.readlines()
f.close()
flag_sosaniy = True

async def get_com(message: types.Message):
    if message.content_type == 'photo' and (message.text == '/sosal' or message.caption =='/sosal'):
        await message.answer(rd.choice(comment))
    elif message.content_type != 'photo' and message.text == '/sosal':
        await message.answer(' Видимо ты орально фиксируешься недостаточно!\nБыстро прислал фото! ')

def get_com_choice():
    return rd.choice(comment)

async def get_comSOS(message: types.Message):
    bd.write_user(message.chat.id, message.from_user.id)

async def check_sos(message: types.Message):
    if message.content_type == 'photo' and (message.text == '/sosal' or message.caption =='/sosal'):
        global flag_sosaniy 
        flag_sosaniy = False
        await message.answer(rd.choice(comment))
    else:
        await message.answer(' Видимо ты орально фиксируешься недостаточно!\nБыстро прислал фото! '), True

async def initialize_photo(message: types.Message):
    """Заносим в бд адрес идентефикационного фото"""
    if message.content_type == 'photo':
        if(neuro.detect_face(message.photo)):
            bd.save_image(message.from_user.id, message.photo[-1].file_id)
            await message.answer("Большое спасибо!")
        else:
            await message.answer("На фото не лицо, я извиняюсь, а жопа")
    else:
        await message.answer("Прошу вас, отправьте мне фото вашего лица!")

async def upgrade_photo(message: types.Message):
    """Добавляет на фото оффсет"""
    if message.content_type == 'photo':
        return 0
    else:
        await message.answer("Прошу вас, отправьте мне фото вашего лица!")
    