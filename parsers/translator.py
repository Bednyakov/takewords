'''Модуль для перевода слов из текстового файла и создания словаря.'''

from googletrans import Translator
import os

def progress(func):
    '''Декоратор, сигнализирующий, что функция не зависла'''
    def inner():
        print(f'Выполняется функция {func.__name__}. Это может занять несколько минут.')
        result = func()
        print(f'Функция {func.__name__} успешно выполнена.\n')
        return result
    return inner

@progress
def en_ru_translator(filename: str='words.txt') -> None:
    '''Функция переводит все слова в переданном файле и создает новый файл-словарь'''
    translator = Translator()
    with open('en_ru_file.txt', 'a', encoding='UTF-8') as en_ru_file:
        with open(filename, 'r', encoding='UTF-8') as file:
            for word in file.read().split():
                translation = translator.translate(word, dest='ru')
                en_ru_file.write(f'{word} {translation.text}\n')
    print('4 Ok')

    os.remove('webfile.html')  # Удаляем уже ненужные файлы
    os.remove('text.txt')
    os.remove('words.txt')

if __name__ == '__main__':
    raise Exception('Запущен модуль!')