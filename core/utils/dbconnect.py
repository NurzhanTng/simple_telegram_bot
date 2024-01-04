import psycopg_pool


class Request:
  def __init__(self, connector: psycopg_pool.AsyncConnectionPool.connection) -> None:
    self.connector = connector

  async def add_data(self, user_id: int, user_name: str) -> None:
    query = f"INSERT INTO aiogram_bot_example1.users(user_id, user_name) VALUES ({user_id}, '{user_name}') ON CONFLICT (user_id) DO UPDATE SET user_name = '{user_name}';"
    await self.connector.execute(query)
