import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def search(filename: str) -> set:
    '''Функция ищет слова в файле с помощью регулярного выражения, возвращает множество с результатом.'''
    words = re.compile(r'(\b\w+\b)', re.VERBOSE)
    setwords = set()

    with open(filename, 'r') as file:
        for word in words.findall(file.read()):
            if word.isalpha() and len(word) > 3:
                setwords.add(word.capitalize())

    return setwords

if __name__ == '__main__':
    raise Exception('Запущен модуль!')