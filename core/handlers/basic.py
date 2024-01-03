from aiogram import Bot
from aiogram.types import Message 


async def get_start(message: Message, bot: Bot):
  await bot.send_message(message.from_user.id, f"<b>Привет {message.from_user.username}. Рад тебя видеть!</b>")
  await message.answer(f"<s>Привет {message.from_user.username}. Рад тебя видеть!</s>")
  await message.reply(f"<tg-spoiler>Привет {message.from_user.username}. Рад тебя видеть!</tg-spoiler>")