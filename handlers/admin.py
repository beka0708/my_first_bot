from aiogram import types
from config import bot


async def check_bad_words(message: types.Message):
    bad_words = ("Даун", "Лох", "Тупой")
    if message.chat.type != 'private':
        for words in bad_words:
            if words in message.text:
                user = await message.reply(text='Сообщение содержит запрещенное слово. Кикнуть пользователя??')
                break


async def check_user_is_admin(message: types.Message):
    print(message.chat.type != 'private')
    print(message.text, message.reply_to_message)
    if message.reply_to_message:
        print(message.reply_to_message.text)
    if message.chat.type != 'private':
        admins = await message.chat.get_administrators()
        for admin in admins:
            if admin['user']['id'] == message.from_user.id:
                return True
        return False


async def ban_user(message: types.Message):
    if message.chat.type != 'private':
        admin_author = await check_user_is_admin(message)
        print(f"{admin_author=}")
        if admin_author and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )


async def yes_no(message: types.Message):
    if message.chat.type != 'private':
        admin_ans = await check_user_is_admin(message)
        print(admin_ans)
        if admin_ans and message.reply_to_message:
            # await message.reply(message.reply_to_message.from_user.username)
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )
