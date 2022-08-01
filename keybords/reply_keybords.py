from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Агенти'),
            KeyboardButton(text='Маршрути'),
            KeyboardButton(text='Кліенти')
        ]
    ],
    resize_keyboard=True
)