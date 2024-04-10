import os
import logging
from tools.dbmanager import create_database, insert_data
from parsers import textparser, words_from_text, translator


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(url):
    """Создает БД, вызывает парсеры и создает словарь."""

    if os.path.exists('translation.db') is False:
        create_database()
        logger.info('DB create!')

    if url:
        text_file: str = textparser.parser(url)
        logger.info(f'Textparser ok!')

        words: set = words_from_text.search(text_file)
        logger.info(f'Words search ok!')

        data: list = translator.mediator(words)
        logger.info('Translator ok!')

        insert_data(data)
        logger.info('Translated words added to the database.')


if __name__ == '__main__':
    main(url='https://pypi.org/project/types-aiobotocore-ecr-public/')