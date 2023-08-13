'''Модуль фильтрует словарь от повторений и создает новый словарь'''

def filter(filename: str='en_ru_file.txt'):
    '''
    Функция создает словарь, обновляемый методом dict.update.
    Существующие ключи перезаписываются, тем самым удаляются повторения.
    После чего отфильтрованный словарь записывается в новый файл.
    '''
    newdict = dict()
    with open(filename, 'r', encoding='UTF-8') as wordsfile:
        for line in wordsfile.readlines():
            newdict.update({line.split()[0]: line.split()[1]})

    with open('en_ru_dict.txt', 'w', encoding='UTF-8') as mydict:
        for key, value in newdict.items():
            mydict.writelines(f'{key}:{value}\n')


if __name__ == '__main__':
    raise Exception('Запущен модуль!')