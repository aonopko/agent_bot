from aiogram import types
from keybords.reply_keybords import menu
from inline_keybords.inline_menu import agent_kb
from load_bot import dp


@dp.message_handler(text="/start")
async def start(message: types.Message):
    text = message.text
    await message.answer(text, reply_markup=menu)

@dp.message_handler(text="Агент")
async def start(message: types.Message):
    text = message.text
    await message.answer(text, reply_markup=agent_kb)