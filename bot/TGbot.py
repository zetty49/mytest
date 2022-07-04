from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import dispatcher
from aiogram.utils import executor

import os



bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)



#КЛИЕНТСКАЯ ЧАСТЬ

@dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    
    await bot.send_sticker(message.chat.id, sticker=r'CAACAgIAAxkBAAEFJpJiuu33Vvn5IrFFJObqKj4kSdLEhQACuQIAAjZ2IA7tdOsFZ9JbhSkE' )
    await bot.send_message(message.chat.id, 'Привет я бот созданый miki чтобы быть подопытным кроликом')







executor.start_polling(dp, skip_updates=True)