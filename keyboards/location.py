from telegram import (
    ReplyKeyboardMarkup, KeyboardButton,
)


def get_location_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(text="Location", request_location=True)
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True,
    )

