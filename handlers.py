from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from config import ADMIN_ID
from main import bot

async def start_cmd_handler(message: Message):
    await message.answer("Привет, я ваш бот. Введите /idea чтобы отправить идею.")

async def idea_cmd_handler(message: Message):
    text = message.text
    user = message.from_user
    await bot.send_message(chat_id=ADMIN_ID, text=f"Новая идея от {user.first_name}: {text}")
    await message.answer("Спасибо за вашу идею. Администратор просмотрит ее.")

def setup(dp: Dispatcher):
    dp.register_message_handler(start_cmd_handler, commands=['start'])
    dp.register_message_handler(idea_cmd_handler, commands=['idea'])