from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsTrueContact(BaseFilter):
  async def __call__(self, message: Message):
    try:
      if message.contact.user_id == message.from_user.id:
        return { 'phone': message.contact.phone_number }
    except:
      return False