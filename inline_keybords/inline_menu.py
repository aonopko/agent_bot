from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .callbacks import agent_callback


agent_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text="Додати агента",
                                                            callback_data=agent_callback.new(id_agent=123,
                                                                                             agent_name="Andrey"))
                                   ]
                               ])
