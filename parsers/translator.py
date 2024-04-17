from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count, Pool
from googletrans import Translator
import threading
import logging
import time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

words_in_db = []

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

    if word not in words_in_db:
        translator = Translator()
        try:
            translation = translator.translate(word, dest='ru')
            return f'{word} {translation.text}'
        except Exception as e:
            logger.info(f'Exception: {e}')

def mediator(words: set, session) -> list:
    '''Получает последовательность и в многопоточном режиме вызывает функцию перевода. Возвращает список строк.'''
    start = time.time()
    global words_in_db
    words_in_db = [row.split()[0] for row in session.get_data()]
    with ThreadPool(processes=cpu_count() * 5) as pool:
        result = pool.map(en_ru_translator, words)

    end = time.time()
    logger.info(f'Translator on Thread Pool speed: {end - start}')

    return result

def mediator_cpool(words: set) -> list:
    'Посредник на пуле процессов для экспериментов со скоростью.'
    start = time.time()
    with Pool(processes=cpu_count()) as pool:
        result = pool.map(en_ru_translator, words)

    end = time.time()
    logger.info(f'Translator on CPU Pool speed: {end - start}')
    return result


def mediator_threads(words: set) -> list:
    'Посредник на потоках для экспериментов со скоростью.'
    result = []
    start = time.time()
    lock = threading.Lock()
    def thread_function(word):
        'Использование мьютекса threading.Lock для безопасного доступа к общему ресурсу result.'
        nonlocal result
        translation = en_ru_translator(word)
        with lock:
            result.append(translation)

    # Создание и запуск потоков для вызова функции en_ru_translator
    threads = []
    for word in words:
        thread = threading.Thread(target=thread_function, args=(word,))
        thread.start()
        threads.append(thread)

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    end = time.time()
    logger.info(f'Translator on Threads speed: {end - start}')
    return result


if __name__ == '__main__':
    raise Exception('Запущен модуль!')