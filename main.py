from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import dp
from handlers.admin import (
    check_bad_words,
    check_user_is_admin,
    ban_user,
    yes_no
)
from handlers.filters import IsAdminFilter


dp.filters_factory.bind(IsAdminFilter)
dp.register_message_handler(check_user_is_admin)
dp.register_message_handler(check_bad_words)
dp.register_message_handler(yes_no, commands=['да'], commands_prefix=['!'])
dp.register_message_handler(ban_user, commands=['ban'], commands_prefix='!/')
if __name__ == '__main__':
    print(__name__)

executor.start_polling(dp)


# dp.register_message_handler(cmd_start, commands=['start'])
# dp.register_message_handler(cmd_help, commands=['help'])
# dp.register_message_handler(cmd_picture, commands=['picture'])
# dp.register_message_handler(cmd_info, commands=['myinfo'])
# dp.register_message_handler(show_products, commands=['products'])
# dp.register_message_handler(show_see, Text(equals="Посмотреть гаджеты"))
# dp.register_message_handler(show_price, Text(equals="Узнать цену"))
# dp.register_message_handler(show_shop, Text(equals="Купить гаджет"))
# dp.register_message_handler(show_address, Text(equals="Адрес"))
