from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

greet = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
], resize_keyboard=True)


inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url='https://ru.euronews.com/news/international')],
    [InlineKeyboardButton(text="Музыка", url='https://hitster.fm/')],
    [InlineKeyboardButton(text="Видео", url='https://www.youtube.com/watch?v=tGNxEUa5z9A')]
])

another_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data='more')]
])

my_buttons = ["Опция 1", "Опция 2"]

async def opt_keyboard():
    keyboard = InlineKeyboardBuilder()
    for key in my_buttons:
        keyboard.add(InlineKeyboardButton(text=key, callback_data=key))
    return keyboard.adjust(2).as_markup()