import sqlite3

def create_database(name: str = 'translation') -> None:
    with sqlite3.connect(f'{name}.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS en_ru_dict (
                        id INTEGER PRIMARY KEY,
                        words TEXT)''')


def insert_data(data: list) -> None:
    with sqlite3.connect('translation.db') as conn:
        cursor = conn.cursor()

        for item in data:
            if item is not None:
                count, *_ = cursor.execute(f"SELECT COUNT (*) FROM en_ru_dict WHERE words = '{item}'").fetchone()
                if count == 0:
                    cursor.execute("INSERT INTO en_ru_dict (words) VALUES (?)", (item,))


def get_data() -> list:
    with sqlite3.connect('translation.db') as conn:
        cursor = conn.cursor()

        rows = cursor.execute("SELECT words FROM en_ru_dict").fetchall()
        data = [item[0] for item in rows]

        return data


def delete_word_from_db(word: str) -> None:
    with sqlite3.connect('translation.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM en_ru_dict WHERE words = ?", (word,))



if __name__ == '__main__':
    raise Exception('Hello, it is modul!')