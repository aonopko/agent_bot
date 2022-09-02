import os

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

from dotenv import load_dotenv
from db.postgresql import db

load_dotenv()
storage = MemoryStorage()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)


__all__ = ["storage", "bot", "dp", "db"]
