from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Агенти'),
            KeyboardButton(text='Маршрут'),
            KeyboardButton(text='Кліенти')
        ]
    ],
    resize_keyboard=True
)