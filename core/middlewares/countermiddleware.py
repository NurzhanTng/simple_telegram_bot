from typing import Any, Awaitable, Callable, Coroutine, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject


class CounterMiddleware(BaseMiddleware):
  def __init__(self) -> None:
    self.counter = 0

  async def __call__(
    self, 
    handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
    event: TelegramObject, 
    data: Dict[str, Any]
  ) -> Coroutine[Any, Any, Any]:
    self.counter += 1
    data['counter'] = self.counter
    return await handler(event, data)