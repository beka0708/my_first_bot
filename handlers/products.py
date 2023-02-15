from aiogram import types
import random
from config import bot

kb = types.ReplyKeyboardMarkup()
kb.add(
    types.KeyboardButton("Посмотреть гаджеты")
)
kb.add(
    types.KeyboardButton('Узнать цену')
)
kb.add(
    types.KeyboardButton('Купить гаджет')
)
kb.add(
    types.KeyboardButton('Адрес')
)


async def show_products(message: types.Message):
    chat_id = message.from_user.id
    await message.answer(
        text="Hello",
        reply_markup=kb
    )


async def show_see(message: types.Message):
    ph = (
        'imagess/divan.jpg',
        'imagess/razmer.jpg',
        'imagess/shkaf.jpg'
    )
    photo = open(random.choice(ph), 'rb')
    await message.answer_photo(
        photo=photo,
        caption='Уникальные гаджеты',
        reply_markup=kb
    )


async def show_price(message: types.Message):
    await message.reply('Летающий диван - 1000$\n'
                        'Пальчиковый измерятель - 1500$\n'
                        'Складыватель вещей - 2000$')


async def show_shop(message: types.Message):
    await message.answer('К сожелению у нас не осталось товаров в наличии((\nВ скором времени появятся!!!')


async def show_address(message: types.Message):
    await message.reply('Кыргызская Республика 720004\n'
                        'г. Бишкек, ул. Калык Акиева №83\n'
                        'Тел.: +996 (709)86-39-06\n'
                        'email: jarvis@0708gmail.com')
