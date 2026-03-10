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


# Слушатель событий
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я эхо-бот. Отправь мне любое сообщение, и я его повторю."
    )


# Хэндлер для остальных сообщений
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Я получил твоё сообщение: {message.text}")


# Запуск процесса поллинга новых апдейтов
async def main():
    # Удаляем вебхук и пропускаем накопившиеся входящие сообщения
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


# Точка входа в программу
if __name__ == "__main__":
    asyncio.run(main())
