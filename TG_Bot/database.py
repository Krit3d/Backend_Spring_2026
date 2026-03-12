import sqlite3


def db_start():
    con = sqlite3.connect("users.db")
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, user_id INTEGER UNIQUE, full_name TEXT)"
    )

    con.close()


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


def get_all_users():
    con = sqlite3.connect("users.db")
    cursor = con.cursor()

    cursor.execute("SELECT user_id, full_name FROM users")
    users = cursor.fetchall()

    con.close()

    return users
