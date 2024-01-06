from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMediaVideo
from aiogram import Bot
from aiogram.utils.chat_action import ChatActionSender


async def get_audio(message: Message, bot: Bot):
  audio = FSInputFile(path=r"C:\\Users\\ПК\\Music\\Уроки\\Kiki's Delivery Service - A Town with an Ocean View (Piano Tutorial Synthesia) (256  kbps).mp3", filename='')
  await bot.send_audio(message.chat.id, audio=audio)


async def get_document(message: Message, bot: Bot):
  document = FSInputFile(path=r'C:\\Users\\ПК\Documents\All files\\КЭД ФИТ 2020-2021.pdf')
  await bot.send_document(message.chat.id, document=document, caption="It's a document")


async def get_media_group(message: Message, bot: Bot):
  photo1_mg = InputMediaPhoto(type='photo', media=FSInputFile(path=r'C:\\Users\\ПК\\Pictures\\0001.jpg'), caption="It's mediagroup")
  photo2_mg = InputMediaPhoto(type='photo', media=FSInputFile(path=r'C:\\Users\\ПК\Downloads\bot.png'))
  video_mg = InputMediaVideo(type='video', media=FSInputFile(path=r'C:\\Users\\ПК\\Videos\\Видео Ернара\\XRecorder0\\XRecorder_21082022_120427.mp4'))
  media = [photo1_mg, photo2_mg, video_mg]
  await bot.send_media_group(message.chat.id, media)


async def get_photo(message: Message, bot: Bot):
  photo = FSInputFile(path=r'C:\\Users\\ПК\\Pictures\\0001.jpg')
  await bot.send_photo(message.chat.id, photo=photo)


async def get_sticker(message: Message, bot: Bot):
  sticker = FSInputFile(path=r'C:\\Users\\ПК\Downloads\bot.png')
  await bot.send_sticker(message.chat.id, sticker=sticker)


async def get_video(message: Message, bot: Bot):
  # async with ChatActionSender.upload_video(chat_id=message.chat.id, bot=bot):
  video = FSInputFile(path=r'C:\\Users\\ПК\\Videos\\Видео Ернара\\XRecorder0\\XRecorder_21082022_120427.mp4')
  await bot.send_video(message.chat.id, video=video)


async def get_video_note(message: Message, bot: Bot):
  # async with ChatActionSender.upload_video(chat_id=message.chat.id, bot=bot):

  # Ошибка из-за большого разммера видео и его неправильного соотношения сторон
  video_note = FSInputFile(path=r'C:\\Users\\ПК\\Videos\\Видео Ернара\\XRecorder0\\XRecorder_21082022_120427.mp4')
  await bot.send_video_note(message.chat.id, video_note=video_note)


async def get_voice(message: Message, bot: Bot):
  # async with ChatActionSender.upload_voice(chat_id=message.chat.id, bot=bot):
  voice = FSInputFile(path=r'C:\\Web\\bots\\iogramm_documentation\\simple_usage\\public\\media\\sample4.opus')
  await bot.send_voice(message.chat.id, voice=voice)