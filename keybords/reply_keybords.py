from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Агент'),
            KeyboardButton(text='Маршрут'),
            KeyboardButton(text='Кліенти')
        ]
    ],
    resize_keyboard=True
)