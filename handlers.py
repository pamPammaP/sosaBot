from aiogram import types
import time
import schedule

async def asking():
    await 'Сосал\n'

async def start(message: types.Message):
    await message.answer("Привет!\nНапиши мне что-нибудь!")
 
async def help(message: types.Message):
    await message.answer("Этот бот с удовольствием поможет тебе научиться фиксироваться орально")

async def echo(message: types.Message):
    await message.answer("Сам ты: " + message.text)

# нужна функция которая бы раз в сутки спрашивала что либо
async def are_you_sosal(bot, message: types.Message):  
    schedule.every(10).seconds.do(asking)
    while True:
        schedule.run_pending()
        time.sleep(1)
        await bot.send_message(message.from_user.id, f'Время: {schedule.run_pending()}:{time.minute}')


# Нужна функция на ставила бы вопрос сосания

