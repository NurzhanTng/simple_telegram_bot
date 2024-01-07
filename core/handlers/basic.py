from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message 
import json

from core.keybords.reply import reply_keyboard, loc_tel_poll_keyboard, get_reply_keyboard
from core.keybords.inline import select_macbook, get_inline_keyboard
from core.utils.dbconnect import Request
from core.utils.commands import set_commands 
from core.settings import settings 

router = Router()


@router.startup()
async def start_bot(bot: Bot):
  await set_commands(bot)
  await bot.send_message(settings.bots.admin_id,  text="Бот запущен!")


@router.shutdown()
async def stop_bot(bot: Bot):
  await bot.send_message(settings.bots.admin_id,  text="Бот остановлен!")


@router.message(Command(commands='inline'))
async def get_inline(message: Message, bot: Bot):
  await message.answer(
    f"Привет, {message.from_user.first_name}. Показываю инлайн кнопки:",
    reply_markup=get_inline_keyboard()
  )


@router.message(Command(commands=['start', 'run']))
async def get_start(message: Message, bot: Bot, counter: str, request: Request):
  # await bot.send_message(message.from_user.id, f"<s>Привет {message.from_user.username}. Рад тебя видеть!</s>")
  # await message.reply(f"<tg-spoiler>Привет {message.from_user.username}. Рад тебя видеть!</tg-spoiler>")
  await request.add_data(message.from_user.id, message.from_user.first_name)
  await message.answer(f'Сообщение #{counter}')
  await message.answer(
    f"<b>Привет {message.from_user.username}. Рад тебя видеть!</b>", 
    reply_markup=get_reply_keyboard()
  )


@router.message(F.location)
async def get_location(message: Message, bot: Bot):
  await message.answer(f'Ты оправил локацию!\r\n{message.location.latitude}\r\a{message.location.longitude}')


@router.message(F.photo)
async def get_photo(message: Message, bot: Bot):
  await message.answer(f"Отлично. ")
  file = await bot.get_file(message.photo[-1].file_id)
  await bot.download_file(file.file_path, 'public/img/photo.jpg')


@router.message(F.text == 'Привет')
async def get_hello(message: Message, bot: Bot):
  await message.answer(f"И тебе привет!")
  json_str = json.dumps(message.model_dump(), default=str, indent=2)
  print(json_str)
