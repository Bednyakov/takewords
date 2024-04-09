import os
import logging
from parsers import textparser, words_from_text, translator


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(url):
    """При вызове удаляет словарь, если он уже был создан! Вызывает парсер текста,
    функцию по выделению слов из текста, функцию-переводчик, создает словарь, удаляет лишние файлы."""

    if os.path.exists('en_ru_file.txt'):
        os.remove('en_ru_file.txt')

    text_file = textparser.parser(url)
    logger.info(f'Textparser ok!')

    words = words_from_text.search(text_file)
    logger.info(f'Words search ok!')

    translator.mediator(words)
    logger.info('Translator ok!')

    os.remove('text.txt')
    logger.info('Remove text.txt and words.txt')


if __name__ == '__main__':
    main(url='https://pypi.org/project/types-aiobotocore-ecr-public/')