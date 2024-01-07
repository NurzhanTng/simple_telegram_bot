import asyncio 
import logging 
import psycopg_pool
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher
from aiogram.utils.chat_action import ChatActionMiddleware

from core.handlers import send_media, basic, callback
from core.handlers.appschedule import send_message_cron, send_message_interval, send_message_time
from core.middlewares.countermiddleware import CounterMiddleware
from core.middlewares.dbmiddleware import DbSession
from core.middlewares.officehours import OfficeHoursMiddleware
from core.middlewares.appshedulermiddleware import SchedulerMiddleware
from core.settings import settings 


def create_pool():
  return psycopg_pool.AsyncConnectionPool(f"host={settings.host} port={settings.port} dbname={settings.database} user={settings.user} password={settings.password} connect_timeout={settings.command_timeout}")

def create_scheduled_tasks(bot: Bot) -> AsyncIOScheduler:
  scheduler = AsyncIOScheduler(timezone="Asia/Almaty")
  start_time = datetime.now()
  scheduler.add_job(send_message_time, trigger='date', run_date=start_time + timedelta(seconds=10), kwargs={ 'bot': bot })
  scheduler.add_job(send_message_cron, trigger='cron', hour=start_time.hour, minute=start_time.minute + 1, kwargs={ 'bot': bot })
  scheduler.add_job(send_message_interval, trigger='interval', seconds=60, kwargs={ 'bot': bot })
  scheduler.start()
  return scheduler

async def main(): 
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
  )
  bot  = Bot(settings.bots.bot_token, parse_mode='HTML')
  pool_connect = create_pool()
  scheduler = create_scheduled_tasks(bot)
  dp = Dispatcher()
  
  dp.message.middleware.register(DbSession(pool_connect))
  dp.message.middleware.register(CounterMiddleware())
  dp.message.middleware.register(ChatActionMiddleware())
  dp.message.middleware.register(OfficeHoursMiddleware())
  dp.message.middleware.register(SchedulerMiddleware(scheduler))

  dp.include_routers(send_media.router, basic.router, callback.router)
  
  try:
    await dp.start_polling(bot)
  finally:
    await bot.session.close()

if __name__ == "__main__":
  asyncio.run(main())
