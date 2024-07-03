import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import TOKEN
from googletrans import Translator

import keyboard as kb

from gtts import gTTS
import os

import random
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=kb.greet)

@dp.message(F.text == "Привет")
async def hello_button(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')

@dp.message(F.text == "Пока")
async def hello_button(message: Message):
    await message.answer(f'До свидания, {message.from_user.first_name}!')


@dp.message(Command('link'))
async def link(message: Message):
    await message.answer('Выберите любую ссылку!', reply_markup=kb.inline_keyboard)


@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer('Нажми', reply_markup=kb.another_inline_keyboard)

@dp.callback_query(F.data == 'more')
async def more(callback: CallbackQuery):
    await callback.answer("Кнопки подгружаются", show_alert=True)
    await callback.message.edit_text('Нажмите на нужную опцию!', reply_markup=await kb.opt_keyboard())


@dp.callback_query(F.data.in_(kb.my_buttons))
async def option_selected(callback: CallbackQuery):
    await callback.message.answer(f"Вы выбрали: {callback.data}")


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды:\n /start \n /help \n /hello')


@dp.message(F.photo)
async def save_photo(message: Message):
    list = ['Отлично! Ваше фото будет сохранено в отдельную папку', 'Круто! Сохраняю', 'Принято! Сохраняю в папку', 'Получил и сохранил!']
    rand_answer = random.choice(list)
    await message.answer(rand_answer)
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')


@dp.message(Command('hello'))
async def hello(message: Message):
    hello_list = [ "Пусть сегодня тебя порадует неожиданная приятная новость, которая зарядит энергией на всю неделю",
                      "Пусть каждый час сегодняшнего дня будет наполнен маленькими победами и радостными моментами",
                      "Найди сегодня минутку для себя, чтобы насладиться любимым хобби и почувствовать настоящую радость",
                      "Пусть встреча с интересным человеком или полезная беседа принесет тебе новые знания и вдохновение",
                      "Пусть сегодняшний день подарит тебе возможность сделать что-то доброе для других и почувствовать тепло благодарности"
   ]
    rand_hi = random.choice(hello_list)
    await message.answer(f"Улыбнись сегодняшнему дню! {rand_hi}")

    tts = gTTS(text=rand_hi, lang='ru')
    tts.save('hello.ogg')
    audio = FSInputFile('hello.ogg')
    await bot.send_voice(message.chat.id, audio)
    os.remove('hello.ogg')


# translator = Translator()
# @dp.message()
# async def translate_text(message: Message):
#     translated = translator.translate(message.text, dest='fr')
#     await message.answer(translated.text)


@dp.message(F.text == 'Здравствуйте, можно ваш прайс лист?')
async def aitext(message: Message):
    await message.answer('')



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())