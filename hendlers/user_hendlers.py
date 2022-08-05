from aiogram import types
from aiogram.dispatcher.filters import Command

from inline_keybords.inline_menu import agent_kb
from keybords.reply_keybords import menu
from load_bot import dp


@dp.message_handler(text="/start")
async def start(message: types.Message):
    text = message.text
    await message.answer(text)
