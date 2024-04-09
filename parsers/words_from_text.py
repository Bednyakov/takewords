import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def search(text: str) -> set:
    '''Функция ищет англ. слова в файле с помощью регулярного выражения, возвращает множество с результатом.'''
    pattern = r'\b[a-zA-Z]{3,}\b'
    words = re.compile(pattern, re.VERBOSE)
    result = set()

    for word in words.findall(text)[:200]:
        result.add(word.capitalize())

    return result

if __name__ == '__main__':
    raise Exception('Запущен модуль!')