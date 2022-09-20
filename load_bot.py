import os

import django
from loguru import logger
from aiogram import executor

from create_bot import dp
import hendlers


async def on_startup(dispatcher):
    logger.info("Create connection")
    logger.info("Connection complete")


def setup_django():
    logger.info("Django connect")
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "telegrambot.telegrambot.settings"
    )
    os.environ.update({"DJANGO_ALLOW_ASYNC_UNSAFE": "true"})
    django.setup()
    logger.info("Django connect finishd")




if __name__ == '__main__':
    setup_django()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
