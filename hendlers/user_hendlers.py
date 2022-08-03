from aiogram import types
from aiogram.dispatcher.filters import Command

from inline_keybords.inline_menu import agent_kb
from keybords.reply_keybords import menu
from create_bot import dp


@dp.message_handler()
async def start(message: types.Message):
    await message.reply(text="Ваше меню")
