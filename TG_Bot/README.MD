# 🤖 Async Crypto Telegram Bot

A high-performance, asynchronous Telegram bot built with **aiogram 3** and **aiohttp**. It interacts with the CoinGecko API to fetch real-time cryptocurrency prices and uses a local **SQLite** database for user management and statistics.

## ✨ Key Features & Architecture
- **Fully Asynchronous:** Uses `aiohttp` for non-blocking external API calls.
- **Dependency Injection:** The `aiohttp.ClientSession` is created once at startup and injected into handlers to optimize connection pooling.
- **Graceful Degradation:** The bot caches supported coins at startup but will successfully initialize even if the external API is temporarily unavailable.
- **Database Singleton:** Database connections and SQL queries are encapsulated in a unified `Database` class to prevent connection leaks and SQL injections.
- **Admin Panel:** Built-in commands for blocking/unblocking users and tracking request statistics.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Krit3d/Backend_Spring_2026.git
   cd Backend_Spring_2026/TG_Bot
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   # People like me :) (Git Bash):
   source venv/Scripts/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create a `.env` file in the `TG_Bot` directory and add the following:
   ```env
   BOT_TOKEN=your_telegram_bot_token_here
   ADMIN_ID=your_telegram_user_id_here
   ```

5. **Run the bot:**
   ```bash
   python bot.py
   ```

## 📝 Usage
- `/start` - Register in the database and get a welcome message.
- `/crypto` - Fetch current price for a randomly selected cryptocurrency.
- `/stats` (Admin only) - View user request statistics.
- `/ban <user_id>` / `/unban <user_id>` (Admin only) - Manage user access.