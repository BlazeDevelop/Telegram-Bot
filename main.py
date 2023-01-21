from aiogram import Bot, Dispatcher, executor
from config import TOKEN
import handlers

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    handlers.setup(dp)
    executor.start_polling(dp)