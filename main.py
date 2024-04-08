import os
import time
import logging
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool
from parsers import textparser, words_from_text, translator


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(url):
    """При вызове удаляет словарь, если он уже был создан, вызывает парсер текста,
    функцию по выделению слов из текста, в многопоточном режиме вызывает функцию-переводчик и создает словарь."""

    if os.path.exists('en_ru_file.txt'):
        os.remove('en_ru_file.txt')

    textparser.parser(url)
    logger.info(f'Textparser ok!')

    words_from_text.search()
    logger.info(f'Words search ok!')

    with open('words.txt', 'r', encoding='UTF-8') as file:
        start = time.time()
        words = file.read().split()

        pool = ThreadPool(processes=cpu_count() * 5)
        result = pool.map(translator.en_ru_translator, words)
        pool.close()
        pool.join()
        end = time.time()
        logger.info(f'Translator speed: {start - end}')

    with open('en_ru_file.txt', 'a', encoding='UTF-8') as en_ru_file:
        for item in result:
            en_ru_file.write(f'{item}\n')
    logger.info('Add en_ru file!')

    os.remove('text.txt')
    os.remove('words.txt')
    logger.info('Remove text.txt and words.txt')


if __name__ == '__main__':
    main(url='https://pypi.org/project/types-aiobotocore-ecr-public/')