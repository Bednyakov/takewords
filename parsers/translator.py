from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count
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
    '''Функция переводит переданную строку.'''
    translator = Translator()
    translation = translator.translate(word, dest='ru')
    return f'{word} {translation.text}'

def mediator(words: set) -> str:
    '''Получает последовательность и в многопоточном режиме вызывает функцию перевода. Записывает результат в файл.'''
    start = time.time()
    pool = ThreadPool(processes=cpu_count() * 5)
    result = pool.map(en_ru_translator, words)
    pool.close()
    pool.join()
    end = time.time()
    logger.info(f'Translator speed: {start - end}')

    with open('en_ru_file.txt', 'a', encoding='UTF-8') as en_ru_file:
        for item in result:
            en_ru_file.write(f'{item}\n')
    logger.info('Add en_ru file!')


if __name__ == '__main__':
    raise Exception('Запущен модуль!')