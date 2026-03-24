import aiohttp
import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import basic_handlers, crypto_handler
from config import BOT_TOKEN

# Enable logging of messages to debugging
logging.basicConfig(level=logging.INFO)

# Create main objects
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

RESPONSE_DATA = {"coins": None, "currencies": None}


# Fetching two lists of coins to work with
async def try_fetch_data() -> bool:
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(
                "https://api.coingecko.com/api/v3/coins/list"
            ) as response:
                RESPONSE_DATA["coins"] = await response.json()

            async with session.get(
                "https://api.coingecko.com/api/v3/simple/supported_vs_currencies"
            ) as response:
                RESPONSE_DATA["currencies"] = await response.json()

        except aiohttp.ClientError as e:
            logging.error(f"Connection error: {type(e).__name__}.")
            return False

        except Exception as e:
            logging.error(f"Unexpected error: {type(e).__name__}.")
            return False

        else:
            return True


async def main() -> None:
    # Register routers in dispatcher
    dp.include_router(crypto_handler.router)
    dp.include_router(basic_handlers.router)

    # Make requests and collect them(two lists)
    is_fetched = await try_fetch_data()
    if not is_fetched:
        logging.warning("Bot was launched without data!")

    # Delete hooks and skip incoming messages
    await bot.delete_webhook(drop_pending_updates=True)
    # Start polling process for new updates
    await dp.start_polling(
        bot,
        coins=RESPONSE_DATA.get("coins", []),
        currencies=RESPONSE_DATA.get("currencies", []),
    )


# Entry point
if __name__ == "__main__":
    asyncio.run(main())
