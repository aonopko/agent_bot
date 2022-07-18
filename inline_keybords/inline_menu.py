from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_kb = InlineKeyboardMarkup(row_width=2,
                               inline_keybords=[
                                   [
                                       InlineKeyboardButton(text="Маршрут",
                                                            callback_data=route_callback.new())
                                   ]
                               ])