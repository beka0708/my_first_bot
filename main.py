from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import logging
from config import dp, bot
from handlers.admin import (
    check_user_is_admin,
    check_bad_words,
    ban_user,
    yes_no
)

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    print('good')

dp.register_message_handler(check_user_is_admin)
dp.register_message_handler(check_bad_words)
dp.register_message_handler(yes_no, commands=['да'], commands_prefix='!/')
dp.register_message_handler(ban_user, commands=['ban'], commands_prefix='!/')

executor.start_polling(dp)
