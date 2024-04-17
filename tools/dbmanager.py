import sqlite3
import logging
from _datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ManagerDB:
    def __init__(self, name_db: str, table_db: str):
        self.name = name_db
        self.table = table_db

    def create_database(self) -> None:
        with sqlite3.connect(self.name) as conn:
            cursor = conn.cursor()

            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.table} (
                            id INTEGER PRIMARY KEY,
                            words TEXT)''')

    def insert_requests(self, user_id: str, ip_addr: str, url: str) -> None:
        with sqlite3.connect(self.name) as conn:
            cursor = conn.cursor()

            cursor.execute(f'''CREATE TABLE IF NOT EXISTS requests (
                                    id TEXT,
                                    ip TEXT,
                                    request TEXT,
                                    date TEXT)''')

            cursor.execute(f"""INSERT INTO requests (id, ip, request, date) 
                                    VALUES (?, ?, ?, ?)""", (user_id, ip_addr, url, datetime.now()))

    def insert_data(self, data: list) -> None:
        with sqlite3.connect(self.name) as conn:
            cursor = conn.cursor()

            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.table} (
                                    id INTEGER PRIMARY KEY,
                                    words TEXT)''')

            for item in data:
                if item is not None:
                    count, *_ = cursor.execute(f"SELECT COUNT (*) FROM {self.table} WHERE words = '{item}'").fetchone()
                    if count == 0:
                        cursor.execute(f"INSERT INTO {self.table} (words) VALUES (?)", (item,))

    def get_data(self) -> list:
        with sqlite3.connect(self.name) as conn:
            cursor = conn.cursor()

            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.table}'")
            table_exists = cursor.fetchone()

            if not table_exists:
                return []

            rows = cursor.execute(f"SELECT words FROM {self.table}").fetchall()
            data = [item[0] for item in rows]

            return data

    def delete_word_from_db(self, word: str) -> None:
        with sqlite3.connect(self.name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {self.table} WHERE words = ?", (word,))
            logger.info(f'Delete: {word}')

    def get_count(self) -> int:
        try:
            with sqlite3.connect(self.name) as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT COUNT (*) FROM {self.table}")

                result, *_ = cursor.fetchone()
                return result
        except sqlite3.OperationalError:
            return 0

    @staticmethod
    def get_api_requests(date: str) -> dict:
        try:
            with sqlite3.connect('translation.db') as conn:
                cursor = conn.cursor()
                result = {}

                data = cursor.execute(
                    f"SELECT id, ip, request, date FROM requests WHERE date LIKE '{date}%'").fetchall()

                for item in data:
                    id, ip, request, date = item
                    if result.get(id) is None:
                        result.update({id: [(ip, request, date)]})
                    else:
                        result[id].append((ip, request, date))

                if result:
                    return result
                return {'sorry': ['no', 'data']}
        except sqlite3.OperationalError:
            return {'sorry': ['no', 'data']}


if __name__ == '__main__':
    raise Exception('Hello, it is modul!')