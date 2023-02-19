from aiogram import types
from config import bot
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup, KeyboardButton


async def kick_user(message: types.Message):
    if message.reply_to_message:
        # получаем id пользователя, которого нужно кикнуть
        user_id = message.reply_to_message.from_user.id

        # кикаем пользователя
        await bot.kick_chat_member(chat_id=message.chat.id, user_id=user_id)

        # отправляем сообщение о кике в чат
        await message.reply_to_message.reply("Пользователь кикнут из чата по команде администратора")
    else:
        await message.reply(
            "Для использования этой команды необходимо ответить на сообщение пользователя, которого нужно кикнуть")


# обработчик сообщений

async def check_forbidden_words(message: types.Message):
    # проверяем сообщение на наличие запрещенных слов
    forbidden_words = ['Лох', 'Даун']
    if message.chat.type != 'private':
        for word in forbidden_words:
            if word in message.text:
                # запрашиваем подтверждение на кик пользователя
                user = await message.reply(text="Сообщение содержит запрещенное слово. Кикнуть пользователя?")
                break


async def check_bad_words(message: types.Message):
    bad_words = ("Даун", "Лох", "Тупой")
    if message.chat.type != 'private':
        for words in bad_words:
            if words in message.text:
                user = await message.reply(text='Сообщение содержит запрещенное слово. Кикнуть пользователя??')
                break


#
#
# async def check_user_is_admin(message: types.Message):
#     print(message.chat.type != 'private')
#     print(message.text, message.reply_to_message)
#     if message.reply_to_message:
#         print(message.reply_to_message.text)
#     if message.chat.type != 'private':
#         admins = await message.chat.get_administrators()
#         for admin in admins:
#             if admin['user']['id'] == message.from_user.id:
#                 return True
#         return False
#
#
# async def ban(message: types.Message):
#     user_id = message.reply_to_message.from_user.id
#     chat_id = message.chat.id
#     await bot.kick_chat_member(chat_id=chat_id, user_id=user_id)
#
#
# async def cmd_ban(message: types.Message):
#     await ban(message)
#
#
# async def ban_user(message: types.Message):
#     if message.chat.type != 'private':
#         admin_author = await check_user_is_admin(message)
#         print(f"{admin_author=}")
#         if admin_author and message.reply_to_message:
#             await message.bot.ban_chat_member(
#                 chat_id=message.chat.id,
#                 user_id=message.reply_to_message.from_user.id
#             )
#
#
# async def yes_no(message: types.Message):
#     if message.chat.type != 'private':
#         admin_ans = await check_user_is_admin(message)
#         print(admin_ans)
#         if admin_ans and message.reply_to_message:
#             # await message.reply(message.reply_to_message.from_user.username)
#             await message.bot.ban_chat_member(
#                 chat_id=message.chat.id,
#                 user_id=message.reply_to_message.from_user.id
#             )
