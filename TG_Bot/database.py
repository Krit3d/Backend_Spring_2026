import sqlite3


# Создаём таблицу для зарегистрированных пользователей
def db_start():
    with sqlite3.connect("users.db") as con:
        cur = con.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY, 
                user_id INTEGER UNIQUE, 
                full_name TEXT
            )
        """
        )


# Записываем каждого юзера в users на команду /start
def cmd_insert(user_id, full_name):
    with sqlite3.connect("users.db") as con:
        cur = con.cursor()

        try:
            cur.execute(
                "INSERT OR IGNORE INTO users (user_id, full_name) VALUES (?, ?)",
                (user_id, full_name),
            )
        except sqlite3.Error as e:
            print(f"DB Error: {type(e).__name__}.")


# Показываем список из данных о каждом пользователе(в виде кортежа)
def get_all_users():
    with sqlite3.connect("users.db") as con:
        cur = con.cursor()
        cur.execute("SELECT user_id, full_name FROM users")

        users = cur.fetchall()

    return users


# Создаём таблицу с запросами пользователей
def create_requests_log():
    with sqlite3.connect("users.db") as con:
        cur = con.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS requests_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER REFERENCES users(user_id),
                coin TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """
        )


# Записываем в лог каждый запрос пользователей
def write_into_log(user_id, coin):
    with sqlite3.connect("users.db") as con:
        cur = con.cursor()

        try:
            cur.execute(
                "INSERT INTO requests_log (user_id, coin) VALUES (?, ?)",
                (user_id, coin),
            )
        except sqlite3.Error as e:
            print(f"DB Error: {type(e).__name__}.")
