from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from inline_keybords.callbacks import route_callback

route_kb = InlineKeyboardMarkup(row_width=2,
                               inline_keybords=[
                                   [
                                       InlineKeyboardButton(text="Початкові дані",
                                                            callback_data=route_callback.new(
                                                                initial_readings="initial_readings")
                                                            ),
                                       InlineKeyboardButton(text="Кінцеві дані",
                                                            callback_data=route_callback.new(
                                                                final_readings="final_readings"
                                                            ))
                                   ]
                               ])