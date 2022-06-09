from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='add agent'),
            KeyboardButton(text='add rout')
        ]
    ],
    resize_keyboard=True
)