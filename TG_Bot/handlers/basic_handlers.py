from aiogram import F, types, Router
from aiogram.filters.command import Command
from database import cmd_insert, get_all_users

router = Router()


# Хэндлер для команды /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Hello, {message.from_user.full_name}. I'm at your service. What can I do for you?"
    )
    cmd_insert(message.from_user.id, message.from_user.full_name)


# Хэндлер для команды /help
@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "I am a simple bot-helper. Please, enter your message."
    )


@router.message(Command("admin"))
async def cmd_admin(message: types.Message):
    users = get_all_users()

    if users:
        txt = "List of users:\n"

        for user in users:
            txt += f"ID: {user[0]} | Имя: {user[1]}\n"

        await message.answer(txt)


# Хэндлер для фото
@router.message(F.photo)
async def photo_handler(message: types.Message):
    await message.answer("It's a photo, isn't it? Please, send me a text.")


# Хэндлер для остальных сообщений
@router.message(F.text)
async def echo_handler(message: types.Message):
    if message.text == "secret":
        await message.answer(f"Congratulations! You've found a secret word!")
    else:
        await message.answer(
            f"Your message '{message.text}' has been accepted for processing."
        )
