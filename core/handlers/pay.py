from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


async def order(message: Message, bot: Bot):
  await bot.send_invoice(
    chat_id=message.chat.id,
    title='Покупка через Telegram бот',
    description='Учимся принимать платежи через Telegram бот',
    payload='Payment through a bot',
    provider_token='410694247:TEST:352da402-d738-4d43-8e29-dd6c93063fc3',
    currency='KZT',
    prices=[
      LabeledPrice(
        label='Доступ к секретной информации',
        amount=990_00
      ),
      LabeledPrice(
        label='НДС',
        amount=200_00
      ),
      LabeledPrice(
        label='Скидка',
        amount=-200_00
      ),
      LabeledPrice(
        label='Бонус',
        amount=-400_00
      ),
    ],
    max_tip_amount=5000,
    suggested_tip_amounts=[1000, 2000, 3000, 4000],
    # start_parameter='https://t.me/tng_learn_bot',
    provider_data=None,
    photo_url='https://i.pinimg.com/originals/4b/ab/dc/4babdc185d12c4e338a5ecda7af4b1fd.jpg',
    photo_size=100,
    photo_width=800,
    photo_height=450,
    need_name=True,
    need_phone_number=True,
    need_email=True,
    need_shipping_address=False,
    send_phone_number_to_provider=False,
    send_email_to_provider=False,
    is_flexible=False,
    disable_notification=False,
    protect_content=False,
    reply_to_message_id=None,
    allow_sending_without_reply=True,
    reply_markup=None,
    request_timeout=15
  )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
  await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
  msg = f"Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency}." \
    f'\r\nНаш менеджер получил заявку и уэе набирает Ваш номер телефона.' \
    f'\r\nПока вы можете скачать цифровую версию нашего продукта https:://nztcoder.com'
  await message.answer(msg)