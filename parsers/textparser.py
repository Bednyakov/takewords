import logging
import requests
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#  nltk - модуль на будущее (умеет работать с текстом, приводить в нач. форму слова и т.д.)

standart_url = 'https://pypi.org/project/types-aiobotocore-ecr-public/'

def parser(url: str) -> str:
    '''Парсит текст из HTML страницы и сохраняет в файл, возвращает имя файла.'''
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        article_text = ""

        for paragraph in soup.find_all('p'):
            article_text += paragraph.get_text()

        with open('text.txt', 'w', encoding='utf-8') as file:
            file.write(article_text)
        logger.info('Add text.txt')
        return 'text.txt'

    except Exception as e:
        logger.error(f'The parser generated an error {e}. Retry with standard url.')
        parser(standart_url)

if __name__ == '__main__':
    raise Exception('Запущен модуль!')