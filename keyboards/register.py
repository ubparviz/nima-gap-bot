from telegram import (
    ReplyKeyboardMarkup, KeyboardButton,
)


def get_register_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(text="Ro'yxatdan o'tish"),
            KeyboardButton(text="Bosh Sahifa"),
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True,
    )

