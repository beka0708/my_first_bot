import random

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user = message.from_user.full_name
    await message.answer(
        f"Hello {user}"
    )


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(
        '''
        /start - Запускает бота
        /help - Помощь
        /myinfo - Своя информация
        /picture - Отправляет какое_то фото
        '''
    )


@dp.message_handler(commands=["myinfo"])
async def info(message: types.Message):
    user_id = message.from_user.id
    first = message.from_user.first_name
    nickname = message.from_user.username
    await message.answer(

        f'Ваш ID: {user_id}\n'
        f'Ваше имя: {first}\n' 
        f'Ваш никнейм: {nickname}'

    )


@dp.message_handler(commands=["picture"])
async def picture(message: types.Message):
    print(message)
    ph = (
        'imagess/jarvis.jpg',
        'imagess/jarvis2.jpg'
    )
    photo = open(random.choice(ph), 'rb')
    await message.answer_photo(
            photo=photo,
            caption='"Jarvis" готов к вашим услугам...'
        )


@dp.message_handler()
async def big_latter(message: types.Message):
    print(message)
    if len(message.text) >= 3:
        await message.answer(
            message.text.title()
        )

# @dp.message_handler(lambda message: message.text and len(message.text.split()) >= 3)
# async def handle_upper_case_message(message: types.Message):
#     print(message)
#     await message.answer(
#         message.text.upper()
#     )


executor.start_polling(dp)
