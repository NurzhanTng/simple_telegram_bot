import asyncio 
import logging 
from aiogram import Bot, Dispatcher, Router, types 
from aiogram.types import Message

from core.handlers import get_start
from core.settings import settings 


dp = Dispatcher()

async def start_bot(bot: Bot):
  await bot.send_message(settings.bots.admin_id,  text="Бот запущен!")

async def stop_bot(bot: Bot):
  await bot.send_message(settings.bots.admin_id,  text="Бот остановлен!")

async def main(): 
  logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
  )
  bot  = Bot(settings.bots.bot_token, parse_mode='HTML')
  dp = Dispatcher()

  dp.message.register(get_start)
  dp.startup.register(start_bot)
  dp.shutdown.register(stop_bot)
  
  try:
    await dp.start_polling(bot)
  finally:
    await bot.session.close()

if __name__ == "__main__":
  asyncio.run(main())