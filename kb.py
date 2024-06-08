from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from text import good, norm, bad, back_t

mood_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=good)],
              [KeyboardButton(text=norm)],
              [KeyboardButton(text=bad)]],
    resize_keyboard=True,
    one_time_keyboard=True
)

back_kb = [[InlineKeyboardButton(text = back_t, callback_data="back")]]
back_kb = InlineKeyboardMarkup(inline_keyboard=back_kb)