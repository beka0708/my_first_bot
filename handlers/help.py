from aiogram import types


async def cmd_help(message: types.Message):
    await message.answer(
        '''
        /start - Запускает бота
        /help - Помощь
        /myinfo - Своя информация
        /picture - Отправляет какое_то фото
        '''
    )