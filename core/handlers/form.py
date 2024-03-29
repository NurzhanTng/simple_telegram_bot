from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta

from core.handlers.appschedule import send_message_middleware
from core.utils.statesform import StepForm


router = Router()

@router.message(Command(commands='form'))
async def get_form(message: Message, state: FSMContext):
  await message.answer(f"{message.from_user.first_name}, начинаем заполнять анкету. Ведите свое имя")
  await state.set_state(StepForm.GET_NAME)


@router.message(StepForm.GET_NAME)
async def get_name(message: Message, state: FSMContext):
  await message.answer(f'Твое имя:\r\n{message.text}\r\nТеперь введи фамилию')
  await state.update_data(name=message.text)
  await state.set_state(StepForm.GET_LAST_NAME)


@router.message(StepForm.GET_LAST_NAME)
async def get_last_name(message: Message, state: FSMContext):
  await message.answer(f'Твоя фамилия:\r\n{message.text}\r\nТеперь введи возраст')
  await state.update_data(last_name=message.text)
  await state.set_state(StepForm.GET_AGE)


@router.message(StepForm.GET_AGE)
async def get_age(message: Message, bot: Bot, state: FSMContext, apscheduler: AsyncIOScheduler):
  await message.answer(f'Твой возраст:\r\n{message.text}\r\n')
  await state.update_data(age=message.text)
  context_data = await state.get_data()
  await message.answer(f'Сохраненные даные в машине состояний:\r\n{str(context_data)}')

  name = context_data.get('name')
  last_name = context_data.get('last_name')
  age = context_data.get('age')
  data_user = f'Вот твои данные\r\n' \
    f'Имя {name}\r\n' \
    f'Фамилия {last_name}\r\n' \
    f'Возраст {age}'
  await message.answer(data_user)
  await state.clear()

  apscheduler.add_job(
    send_message_middleware, 
    trigger='date', 
    run_date=datetime.now() + timedelta(seconds=10), 
    kwargs={ 'bot': bot, 'chat_id': message.chat.id }
  )
