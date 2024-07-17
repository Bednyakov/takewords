import sqlite3
from tools.loggers import logger
from _datetime import datetime


class ManagerDB:
    def __init__(self, name_db: str, table_db: str):
        self.name = name_db
        self.table = table_db

        with sqlite3.connect(self.name) as conn:
            cursor = conn.cursor()

            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.table} (
                            id INTEGER PRIMARY KEY,
                            words TEXT)''')

    def insert_requests(self, user_id: str, ip_addr: str, url: str) -> None:
        """
        Добавляет записи в таблицу requests.
        """
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
        """
        Добавляет запись из пары слов в таблицу юзера.
        """
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
        """
        Получает и возвращает весь список ин. слов из таблицы юзера, если таблица есть.
        """
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
        """
        Удаляет пару слов из таблицы юзера.
        """
        with sqlite3.connect(self.name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {self.table} WHERE words = ?", (word,))
            logger.info(f'Delete: {word}')

    def get_count(self) -> int:
        """
        Возвращает количество записей в таблице юзера.
        """
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
        """
        Возвращает словарь с id, ip и запросами по дате.
        """
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

                return {'sorry': ['no', 'data']}, 404
        except sqlite3.OperationalError:
            return {'sorry': ['no', 'data']}, 404

    @staticmethod
    def get_user_url(username: str) -> list:
        """
        Возвращает словарь с запросами по юзернейму.
        """
        try:
            with sqlite3.connect('translation.db') as conn:
                cursor = conn.cursor()
                result = {}

                data = cursor.execute(
                    f"SELECT request FROM requests WHERE id = '{username}'").fetchall()

                for item in data:
                    url, *_ = item
                    if result.get(username) is None:
                        result.update({username: [url]})
                    else:
                        result[username].append(url)

                if result:
                    return result

                return {'sorry': ['no', 'data']}, 404
        except sqlite3.OperationalError:
            return {'sorry': ['no', 'data']}, 404



if __name__ == '__main__':
    raise Exception('Hello, it is modul!')