from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery

from states.route_state import Agent
from keybords.reply_keybords import menu
#from inline_keybords.inline_menu import agent_kb
from inline_keybords.callbacks import agent_callback
from load_bot import dp


@dp.message_handler(text="/start")
async def start(message: types.Message):
    text = message.text
    await message.answer(text, reply_markup=menu)


def get_agent_kb():
    buttons = [
        types.InlineKeyboardButton(text="Додати агента", callback_data="add_agent")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


@dp.message_handler(text="Агент")
async def start(message: types.Message):
    text = message.text
    await message.answer(text, reply_markup=get_agent_kb())


@dp.callback_query_handler(Text(startswith="add_agent"))
async def add_agent(call: types.CallbackQuery, callback_data: dict):
    agent_name = callback_data.get("id_agent")
    await call.message.answer(f"{agent_name}")
