from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
import logging
from config import dp, bot

logging.basicConfig(level=logging.INFO)

# список запрещенных слов
forbidden_words = ['Лох', 'Даун']


# функция, которая проверяет сообщение на наличие запрещенных слов
async def check_forbidden_words(message: types.Message):
    for word in forbidden_words:
        if word in message.text:
            return True
    return False


# обработчик команды /kick
@dp.message_handler(commands=['kick'])
async def kick_user(message: types.Message):
    if message.reply_to_message:
        await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await bot.send_message(message.chat.id,
                               f"Пользователь {message.reply_to_message.from_user.mention} был забанен админом{message.from_user.mention}")
    else:
        await bot.send_message(message.chat.id, "Пожалуйста, ответьте на сообщение пользователя, чтобы выгнать.")


# обработчик входящих сообщений
@dp.message_handler()
async def handle_message(message: types.Message):
    if message.from_user.is_bot:
        return

    if await check_forbidden_words(message):
        await bot.send_message(message.chat.id, message.message_id)
        await bot.send_message(message.chat.id,
                               f"Пользователь {message.from_user.mention} использовал запрещенные слова и будет забанен "
                               f"администратором")
        await kick_user(message)


if __name__ == '__main__':
    print('good')
    executor.start_polling(dp, skip_updates=True)

# dp.message_handler(ban_user, commands=['ban'], commands_prefix='!/')
# dp.register_message_handler(yes_no, commands=['ban'], commands_prefix=['!/'])
# dp.register_message_handler(check_bad_words)
# dp.register_message_handler(check_bad_words, content_types=['text'])
# dp.register_message_handler(cmd_ban)
# dp.register_message_handler(ban, commands=['ban'], commands_prefix=['!/'])
# dp.message_handler(commands=['kick'])
# if __name__ == '__main__':
#     print(__name__)
#
#
# executor.start_polling(dp)

# dp.register_message_handler(cmd_start, commands=['start'])
# dp.register_message_handler(cmd_help, commands=['help'])
# dp.register_message_handler(cmd_picture, commands=['picture'])
# dp.register_message_handler(cmd_info, commands=['myinfo'])
# dp.register_message_handler(show_products, commands=['products'])
# dp.register_message_handler(show_see, Text(equals="Посмотреть гаджеты"))
# dp.register_message_handler(show_price, Text(equals="Узнать цену"))
# dp.register_message_handler(show_shop, Text(equals="Купить гаджет"))
# dp.register_message_handler(show_address, Text(equals="Адрес"))
