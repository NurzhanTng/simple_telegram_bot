import asyncio 
import logging 
import psycopg_pool
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command

from core.handlers.basic import get_start, get_photo, get_hello, get_location, get_inline
from core.handlers.contact import get_fake_contact, get_true_contact
from core.handlers.callback import select_macbook
from core.handlers.pay import order, pre_checkout_query, successful_payment
from core.handlers.form import get_form, get_name, get_last_name, get_age
from core.handlers.appschedule import send_message_cron, send_message_interval, send_message_time

from core.filters.iscontact import IsTrueContact

from core.utils.commands import set_commands 
from core.utils.callbackdata import MacInfo
from core.utils.statesform import StepForm

from core.middlewares.countermiddleware import CounterMiddleware
from core.middlewares.officehours import OfficeHoursMiddleware
from core.middlewares.dbmiddleware import DbSession
from core.middlewares.appshedulermiddleware import SchedulerMiddleware

from core.settings import settings 

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())



async def start_bot(bot: Bot):
  await set_commands(bot)
  await bot.send_message(settings.bots.admin_id,  text="Бот запущен!")

async def stop_bot(bot: Bot):
  await bot.send_message(settings.bots.admin_id,  text="Бот остановлен!")

def contact_type(message: Message):
  return message.contact

def location_type(message: Message):
  return message.location

def successful_payment_type(message: Message):
  return message.successful_payment

def create_pool():
  return psycopg_pool.AsyncConnectionPool(f"host={settings.bots.host} port={settings.bots.port} dbname={settings.bots.database} user={settings.bots.user} password={settings.bots.password} connect_timeout={settings.bots.command_timeout}")


async def main(): 
  logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
  )
  bot  = Bot(settings.bots.bot_token, parse_mode='HTML')
  pool_connect = create_pool()
  dp = Dispatcher()
  scheduler = AsyncIOScheduler(timezone="Asia/Almaty")
  start_time = datetime.now()
  scheduler.add_job(send_message_time, trigger='date', run_date=start_time + timedelta(seconds=10), kwargs={ 'bot': bot })
  scheduler.add_job(send_message_cron, trigger='cron', hour=start_time.hour, minute=start_time.minute + 1, kwargs={ 'bot': bot })
  scheduler.add_job(send_message_interval, trigger='interval', seconds=60, kwargs={ 'bot': bot })
  scheduler.start()
  
  dp.message.middleware.register(DbSession(pool_connect))
  dp.message.middleware.register(CounterMiddleware())
  dp.message.middleware.register(OfficeHoursMiddleware())
  dp.message.middleware.register(SchedulerMiddleware(scheduler))

  dp.startup.register(start_bot)
  dp.shutdown.register(stop_bot)
  dp.message.register(get_form, Command(commands='form'))
  dp.message.register(get_name, StepForm.GET_NAME)
  dp.message.register(get_last_name, StepForm.GET_LAST_NAME)
  dp.message.register(get_age, StepForm.GET_AGE)
  dp.message.register(get_start, Command(commands=['start', 'run']))
  dp.message.register(get_inline, Command(commands='inline'))
  dp.callback_query.register(select_macbook, MacInfo.filter(F.model == 'pro'))
  dp.message.register(order, Command(commands=['pay']))
  dp.pre_checkout_query.register(pre_checkout_query)
  dp.message.register(successful_payment, successful_payment_type)
  dp.message.register(get_photo, F.photo)
  dp.message.register(get_hello, F.text == 'Привет')
  dp.message.register(get_location, location_type)
  dp.message.register(get_true_contact, contact_type, IsTrueContact())
  dp.message.register(get_fake_contact, contact_type)
  
  try:
    await dp.start_polling(bot)
  finally:
    await bot.session.close()

if __name__ == "__main__":
  asyncio.run(main())
  # print(datetime.datetime.now(datetime.timezone.utc).astimezone())