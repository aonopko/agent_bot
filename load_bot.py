import os

import django
from loguru import logger
from aiogram import executor

from create_bot import dp, db
import hendlers


async def on_startup(dp):
    logger.info('Create connection')
    logger.info('Connection complete')


def setup_django():
    logger.info("CREATE DJANGO CONNECTION")
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "telegrambot.django_project.settings"
    )
    os.environ.update({"DJANGO_ALLOW_ASYNC_UNSAFE": "true"})
    logger.info("DJANGO WAS CONNECT")


if __name__ == '__main__':
    setup_django()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
