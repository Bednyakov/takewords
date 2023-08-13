'''Модуль для создания файла со словами'''

import re

def search(filename: str='text.txt'):
    '''Функция ищет слова в файле с помощью регулярного выражения
    и создает новый файл words.txt'''
    words = re.compile(r'(\b\w+\b)', re.VERBOSE)

    with open('words.txt', 'a') as wordsfile:
        with open(filename, 'r') as file:

            for word in words.findall(file.read()):
                if word.isalpha() and len(word) > 3:
                    wordsfile.writelines(f'{word.capitalize()}\n')


if __name__ == '__main__':
    raise Exception('Запущен модуль!')