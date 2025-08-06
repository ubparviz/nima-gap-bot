from telegram import (
    InlineKeyboardMarkup, InlineKeyboardButton,
)


def get_language_keyboard() -> InlineKeyboardMarkup:
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Uzbek', callback_data='lang:uz'), 
            InlineKeyboardButton(text='English', callback_data='lang:en')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard)
