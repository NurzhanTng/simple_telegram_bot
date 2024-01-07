from environs import Env
from dataclasses import dataclass


@dataclass 
class Bots:
  bot_token: str
  admin_id: int

@dataclass
class Settings:
  bots: Bots
  user: str
  password: str 
  database: str 
  host: str
  port: int
  command_timeout: int
  options: str


def get_settings(path: str):
  env = Env()
  env.read_env(path)

  return Settings(
    bots=Bots(
      bot_token=env.str("BOT_TOKEN"),
      admin_id=env.int("ADMIN_ID"),
    ),
    user=env.str("USER"),
    password=env.str("PASSWORD"),
    database=env.str("DATABASE"),
    host=env.str("HOST"),
    port=env.int("PORT"),
    command_timeout=env.int("COMMAND_TIMEOUT"),
    options=env.str("OPTIONS"),
  )

settings = get_settings('.env')
