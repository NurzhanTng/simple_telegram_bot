import asyncio 
import logging 
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command

from core.handlers.basic import get_start, get_photo, get_hello, get_location
from core.handlers.contact import get_fake_contact, get_true_contact
from core.filters.iscontact import IsTrueContact
from core.utils.commands import set_commands 
from core.settings import settings 


async def start_bot(bot: Bot):
  await set_commands(bot)
  await bot.send_message(settings.bots.admin_id,  text="Бот запущен!")

async def stop_bot(bot: Bot):
  await bot.send_message(settings.bots.admin_id,  text="Бот остановлен!")

def contact_type(message: Message):
  return message.contact

def location_type(message: Message):
  return message.location

async def main(): 
  logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
  )
  bot  = Bot(settings.bots.bot_token, parse_mode='HTML')
  
  dp = Dispatcher()
  dp.message.register(get_start, Command(commands=['start', 'run']))
  dp.message.register(get_photo, F.photo)
  dp.message.register(get_hello, F.text == 'Привет')
  dp.message.register(get_location, location_type)
  dp.message.register(get_true_contact, contact_type, IsTrueContact())
  dp.message.register(get_fake_contact, contact_type)
  dp.startup.register(start_bot)
  dp.shutdown.register(stop_bot)
  
  try:
    await dp.start_polling(bot)
  finally:
    await bot.session.close()

if __name__ == "__main__":
  asyncio.run(main())