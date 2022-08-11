from aiogram import types
from aiogram.types import CallbackQuery

from keybords.reply_keybords import menu
from inline_keybords.inline_menu import agent_kb
from inline_keybords.callbacks import agent_callback
from load_bot import dp


@dp.message_handler(text="/start")
async def start(message: types.Message):
    text = message.text
    await message.answer(text, reply_markup=menu)


@dp.message_handler(text="Агент")
async def start(message: types.Message):
    text = message.text
    await message.answer(text, reply_markup=agent_kb)


@dp.callback_query_handler(agent_callback.filter(id_agent=123))
async def add_agent(call: CallbackQuery, callback_data: dict):
    await call.answer(text="Добавляем")
    agent_name = callback_data.get("agent_name")
    await call.message.answer(f"{agent_name}")
