"""create file key.py and make this imported arrays in it"""
from key import api_key, telegram_key, yulia_prompt # you can customize Yulia, just write prompt who you need in array "yulia_prompt"
from gpytranslate import SyncTranslator
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from Yulia import dialog_with_yulia

bot = Bot(telegram_key)
dp = Dispatcher(bot)


@dp.message_handler()
async def send(message: types.Message):
    username = message.from_user.username
    if message.text == "Clear":
        with open('memory.txt', 'w') as f:
            f.write(yulia_prompt)
    elif message.text == "/start":
        pass
    else:
        yulia_message = dialog_with_yulia(message.text, username)
        await message.answer(yulia_message)


executor.start_polling(dp, skip_updates=True)