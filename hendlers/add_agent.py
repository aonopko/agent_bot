from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from asyncpg.exceptions import UniqueViolationError


from arles.inline_keybords.inline_kb import get_agent_kb, button_ok
from arles.states.route_state import AgentState
from arles.keybords.reply_keybords import menu
from arles.load_bot import dp


@dp.message_handler(text="/start")
async def start(message: types.Message):
    text = message.text
    await message.answer(text, reply_markup=menu)


@dp.message_handler(text="Агент")
async def start(message: types.Message):
    await message.answer(text="МЕНЮ АГЕНТА",
                         reply_markup=get_agent_kb())


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
        await call.message.answer(f"Агент с ID {data.get('id_agent')} додано")
    await call.answer()
    await state.finish()
