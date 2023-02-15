from aiogram import types


async def cmd_start(message: types.Message):
    user = message.from_user.full_name
    await message.reply(
        f"Hello {user}\n Здесь ты можешь продать или купить современные гаджеты "
    )



