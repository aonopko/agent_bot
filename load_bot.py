import os

import django
from loguru import logger
from aiogram import executor

from create_bot import dp, db
import hendlers


async def on_startup(dp):
    logger.info('Create connection')
    logger.info('Connection complete')





if __name__ == '__main__':
    #setup_django()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
