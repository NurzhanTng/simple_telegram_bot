from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
  commands = [
    BotCommand(
      command='start',
      description='Начало работы'
    ),
    BotCommand(
      command='help',
      description='Помощь'
    ),
    BotCommand(
      command='cancel',
      description='Сбросить'
    ),
    BotCommand(
      command='inline',
      description='Показать инлайн кнопки'
    ),
    BotCommand(
      command='pay',
      description='Купить продукт'
    ),
    BotCommand(
      command='form',
      description='Начать опрос'
    ),
    BotCommand(
      command='audio',
      description='Прислать аудио'
    ),
    BotCommand(
      command='document',
      description='Прислать документ'
    ),
    BotCommand(
      command='mediagroup',
      description='Прислать медиагруппу'
    ),
    BotCommand(
      command='photo',
      description='Прислать фотографию'
    ),
    BotCommand(
      command='sticker',
      description='Прислать стикер'
    ),
    BotCommand(
      command='video',
      description='Прислать видео'
    ),
    BotCommand(
      command='video_note',
      description='Прислать видео сообщение'
    ),
    BotCommand(
      command='voice',
      description='Прислать голосовое сообщение'
    ),
  ]

  await bot.set_my_commands(commands, BotCommandScopeDefault())