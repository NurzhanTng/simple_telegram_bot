from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from psycopg_pool import AsyncConnectionPool

from core.utils.dbconnect import Request


class DbSession(BaseMiddleware):
  def __init__(self, connector: AsyncConnectionPool) -> None:
    super().__init__()
    self.connector = connector

  async def __call__(
    self, 
    handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
    event: TelegramObject, 
    data: Dict[str, Any]
  ) -> Any:
    async with self.connector.connection() as connect:
      data['request'] = Request(connect)
      return await handler(event, data)