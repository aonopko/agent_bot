from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            KeyboardButton(text='Маршрут'),
            KeyboardButton(text='Кліенти')
        ]
    ],
    resize_keyboard=True
)