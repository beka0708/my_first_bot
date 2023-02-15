from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import dp
from handlers.start import cmd_start
from handlers.help import cmd_help
from handlers.picture import cmd_picture
from handlers.my_info import cmd_info
from handlers.products import (
    show_products,
    show_see,
    show_price,
    show_shop,
    show_address
)

if __name__ == '__main__':
    print(__name__)
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(cmd_help, commands=['help'])
    dp.register_message_handler(cmd_picture, commands=['picture'])
    dp.register_message_handler(cmd_info, commands=['myinfo'])
    dp.register_message_handler(show_products, commands=['products'])
    dp.register_message_handler(show_see, Text(equals="Посмотреть гаджеты"))
    dp.register_message_handler(show_price, Text(equals="Узнать цену"))
    dp.register_message_handler(show_shop, Text(equals="Купить гаджет"))
    dp.register_message_handler(show_address, Text(equals="Адрес"))

executor.start_polling(dp)
