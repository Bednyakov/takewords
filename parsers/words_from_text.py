'''Модуль для создания файла со словами'''

import re
from parsers import translator

def search(filename: str='text.txt'):
    '''Функция ищет слова в файле с помощью регулярного выражения
    и создает новый файл words.txt'''
    words = re.compile(r'(\b\w+\b)', re.VERBOSE)
    setwords = set()
    with open('words.txt', 'w') as wordsfile:
        with open(filename, 'r') as file:

            for word in words.findall(file.read()):
                if word.isalpha() and len(word) > 3:
                    setwords.add(word.capitalize())  # Фильтруем слова от повторений с помощью множества

            for word in setwords:
                wordsfile.writelines(f'{word}\n')
    print('3 Ok')

    translator.en_ru_translator()

if __name__ == '__main__':
    raise Exception('Запущен модуль!')