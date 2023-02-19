from aiogram import types


async def cmd_info(message: types.Message):
    print(message)
    user_id = message.from_user.id
    first = message.from_user.first_name
    nickname = message.from_user.username
    await message.answer(

        f'Ваш ID: {user_id}\n'
        f'Ваше имя: {first}\n'
        f'Ваш никнейм: {nickname}'

    )

