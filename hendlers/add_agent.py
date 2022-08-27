from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from asyncpg.exceptions import UniqueViolationError

from db.db_commands import add_agent
from states.route_state import AgentState
from keybords.reply_keybords import menu
from load_bot import dp


@dp.message_handler(text="/start")
async def start(message: types.Message):
    text = message.text
    await message.answer(text, reply_markup=menu)


def get_agent_kb():
    buttons = [
        types.InlineKeyboardButton(text="Додати агента", callback_data="add_agent"),
        types.InlineKeyboardMarkup(text="Видалити агента", callback_data="del_agent")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def button_ok():
    button = [types.InlineKeyboardButton(text="OK",
                                         callback_data="OK")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*button)
    return keyboard


@dp.message_handler(text="Агент")
async def start(message: types.Message):
    text = message.text
    await message.answer(text, reply_markup=get_agent_kb())


@dp.callback_query_handler(Text(startswith="add_agent"))
async def add_agent_name(call: types.CallbackQuery):
    await call.message.answer("Введіть Ім'я")
    await call.answer()
    await AgentState.agent_name.set()


@dp.message_handler(state=AgentState.agent_name)
async def add_id_agent(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["agent_name"] = message.text
        await AgentState.id_agent.set()
        await message.answer(f"Натисніть  OK для завершення",
                             reply_markup=button_ok())


@dp.callback_query_handler(Text(startswith="OK"),
                           state=AgentState.id_agent)
async def get_id_name(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["id_agent"] = call.from_user.id
    try:
        await add_agent(agent_id=data.get("id_agent"),
                        agent_name=data.get("agent_name"))
    except UniqueViolationError:
        get_id = data.get("id_agent")
        await call.message.reply(f"УВАГА\n"
                                 f"Агент з id {get_id} існує",
                                 reply_markup=menu)
    else:
        await call.message.reply("Ваш id додано")
        await call.answer()

    await state.finish()
