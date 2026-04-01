from pydantic import EmailStr
from fastapi import HTTPException
import sqlite3


def create_table() -> None:
    with sqlite3.connect("users.db") as con:
        cur = con.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY, 
                username TEXT,
                age INTEGER,
                email TEXT UNIQUE
            )
        """
        )


def add_user(username: str, age: int, email: EmailStr) -> int | None:
    with sqlite3.connect("users.db") as con:
        cur = con.cursor()

        try:
            cur.execute(
                """
                INSERT INTO users (username, age, email) VALUES (?, ?, ?)
                """,
                (username, age, email),
            )
        except sqlite3.IntegrityError:
            raise HTTPException(status_code=409, detail="User already exists!")
        else:
            con.commit()

            return cur.lastrowid


def get_all_users() -> list[dict]:
    with sqlite3.connect("users.db") as con:
        cur = con.cursor()

        cur.execute("SELECT * FROM users")
        columns = [desc[0] for desc in cur.description]
        results = cur.fetchall()
        return [dict(zip(columns, row)) for row in results]
