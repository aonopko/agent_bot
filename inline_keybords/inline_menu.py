from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


agent_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text="Додати агента", url="https://github.com/"),
                                       InlineKeyboardButton(text="Видалити агента", url="https://github.com/")
                                   ]
                               ])
