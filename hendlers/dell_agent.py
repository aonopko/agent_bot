from aiogram import types
from aiogram.dispatcher.filters import Text

from load_bot import dp



@dp.callback_query_handler(Text(startswith="del_agent"))
async def delete_agent(call: types.CallbackQuery):
    id_agent = call.from_user.id
    await del_agent(agent_id=id_agent)
    await call.answer(f"агента {id_agent} ВИДАЛЕНО")
