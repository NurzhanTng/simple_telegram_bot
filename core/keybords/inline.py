from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder  

from core.utils.callbackdata import MacInfo


select_macbook = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(
        text='Mackbook Air 13" M1 2020',
        callback_data='apple_air_13_m1_2020'
      )
    ],
    [
      InlineKeyboardButton(
        text='Mackbook Air 14" M1 Pro 2021',
        callback_data='apple_air_14_m1_2021'
      )
    ],
    [
      InlineKeyboardButton(
        text='Apple Mackbook Pro 16" 2019',
        callback_data='apple_pro_16_i7_2019'
      )
    ],
    [ 
      InlineKeyboardButton(
        text='Links',
        url='https://google.com'
      )
    ],
    [ 
      InlineKeyboardButton(
        text='Profile',
        url='tg://user?id=1234249296'
      )
    ]
  ]
)


def get_inline_keyboard():
  keyboard_builder = InlineKeyboardBuilder()
  
  keyboard_builder.button(text='Mackbook Air 13" M1 2020', callback_data=MacInfo(model='air', size=13, chip='m1', year=2020))
  keyboard_builder.button(text='Mackbook Pro 14" M1 Pro 2021', callback_data=MacInfo(model='pro', size=14, chip='m1', year=2021))
  keyboard_builder.button(text='Apple Mackbook Pro 16" 2019', callback_data=MacInfo(model='pro', size=16, chip='i7', year=2019))
  keyboard_builder.button(text='Links', url='https://google.com')
  keyboard_builder.button(text='Profile', url='tg://user?id=1234249296')
  keyboard_builder.adjust(3)

  return keyboard_builder.as_markup()