from aiogram import types


def get_agent_kb():
    buttons = [
        types.InlineKeyboardButton(text="Додати агента",
                                   callback_data="add_agent"),
        types.InlineKeyboardMarkup(text="Видалити агента",
                                   callback_data="del_agent"),
        types.InlineKeyboardMarkup(text="Дані агента",
                                   callback_data="data_agent")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    return keyboard


def button_ok():
    button = [types.InlineKeyboardButton(text="OK",
                                         callback_data="OK")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*button)
    return keyboard
