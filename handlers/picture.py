import random
from aiogram import types


async def cmd_picture(message: types.Message):
    ph = (
        'imagess/jarvis.jpg',
        'imagess/jarvis2.jpg'
    )
    photo = open(random.choice(ph), 'rb')
    await message.answer_photo(
        photo=photo,
        caption='"Jarvis" готов к вашим услугам...'
    )
