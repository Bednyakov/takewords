from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count
from tools.dbmanager import get_data
from googletrans import Translator
import logging
import time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def progress(func):
    '''Декоратор, сигнализирующий, что функция не зависла.'''
    def inner(arg):
        result = func(arg)
        logger.info(f'Функция {func.__name__} обработала {arg}.')
        return result
    return inner

@progress
def en_ru_translator(word: str) -> str:
    '''Функция переводит переданную строку, если её нет в БД.'''
    words_in_db = get_data()
    if word not in words_in_db:
        translator = Translator()
        try:
            translation = translator.translate(word, dest='ru')
            return f'{word} {translation.text}'
        except Exception as e:
            logger.info(f'Exception: {e}')

def mediator(words: set) -> list:
    '''Получает последовательность и в многопоточном режиме вызывает функцию перевода. Возвращает список строк.'''
    start = time.time()
    pool = ThreadPool(processes=cpu_count() * 5)
    result = pool.map(en_ru_translator, words)
    pool.close()
    pool.join()
    end = time.time()
    logger.info(f'Translator speed: {start - end}')

    return result


if __name__ == '__main__':
    raise Exception('Запущен модуль!')