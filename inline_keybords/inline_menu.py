from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from inline_keybords.callbacks import agent_callback

agent_kb = InlineKeyboardMarkup(row_width=2,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text="Додати агента",
                                                            callback_data=agent_callback.new(
                                                                add_agent="add_agent")
                                                            ),
                                       InlineKeyboardButton(text="Видалити агента",
                                                            callback_data=agent_callback.new(
                                                                del_agent="del_agent"
                                                            ))
                                   ]
                               ])
