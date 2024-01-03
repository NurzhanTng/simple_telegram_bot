from aiogram import Bot
from aiogram.types import Message 
import json


async def get_start(message: Message, bot: Bot):
  await bot.send_message(message.from_user.id, f"<b>Привет {message.from_user.username}. Рад тебя видеть!</b>")
  await message.answer(f"<s>Привет {message.from_user.username}. Рад тебя видеть!</s>")
  await message.reply(f"<tg-spoiler>Привет {message.from_user.username}. Рад тебя видеть!</tg-spoiler>")

async def get_photo(message: Message, bot: Bot):
  await message.answer(f"Отлично. ")
  file = await bot.get_file(message.photo[-1].file_id)
  await bot.download_file(file.file_path, 'public/img/photo.jpg')

async def get_hello(message: Message, bot: Bot):
  await message.answer(f"И тебе привет!")
  json_str = json.dumps(message.model_dump(), default=str, indent=2)
  print(json_str)