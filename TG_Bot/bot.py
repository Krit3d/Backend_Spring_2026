import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import BOT_TOKEN

# Включаем логгирование сообщений для отладки
logging.basicConfig(level=logging.INFO)

# Создаём основные объекты: бот и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Хэндлер для команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Приветствую, сударь. Я к вашим услугам. Чем могу быть полезен?"
    )


# Хэндлер для команды /help
@dp.message(Command("help"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Я простой эхо-бот. Просто отправь мне личное сообщение, и я тебе его верну"
    )


# Хэндлер для остальных сообщений
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(
        f"Я не был запрограммирован на юмор, сударь. Я лишь повторяю ваши фразы: {message.text}"
    )


# Запуск процесса поллинга новых апдейтов
async def main():
    # Удаляем вебхук и пропускаем накопившиеся входящие сообщения
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


# Точка входа в программу
if __name__ == "__main__":
    asyncio.run(main())
