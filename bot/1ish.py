import logging

from aiogram import Bot, Dispatcher, executor, types
 API_TOKEN = '5139240377:AAFaCrB6bsAaWkOzHhieGuFmVV9cysb1zYc'
# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):    """
   This handler will be called when user sends /start or /help command   """
   wait message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
@dp.message_handler()
async def echo(message: types.Message):
   # old style:   # await bot.send_message(message.chat.id, message.text)   await message.answer(message.text)
if name == 'main':executor.start_polling(dp, skip_updates=True)"
 https://docs.aiogram.dev/en/latest/quick_start.html#:~:tex  