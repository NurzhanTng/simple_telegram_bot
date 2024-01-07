from aiogram.types import Message
from aiogram import Bot, Router, F

from core.filters.iscontact import IsTrueContact


router = Router()

@router.message(F.contact, IsTrueContact())
async def get_true_contact(message: Message, bot: Bot, phone: str):
  await message.answer(f'Ты отправил <b>свой</b> контакт {phone}.')
  
@router.message(F.contact)
async def get_fake_contact(message: Message, bot: Bot):
  await message.answer(f'Ты отправил <b>не свой</b> контакт')