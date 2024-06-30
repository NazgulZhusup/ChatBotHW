import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import TOKEN
from googletrans import Translator

from gtts import gTTS
import os

import random
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}! Здесь ты можешь загрузить фото и я сохраню его.  А еще я переведу любой текст на французский язык')

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


translator = Translator()
@dp.message()
async def translate_text(message: Message):
    translated = translator.translate(message.text, dest='fr')
    await message.answer(translated.text)



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())