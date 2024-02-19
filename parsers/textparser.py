'''
Модуль для парсинга текста из элемента веб-страницы
Создает два файла:
1. HTML файл со всем спарсенным кодом
2. TXT файл с текстом из HTML файла
'''

import requests, bs4

#  nltk - модуль на будущее (умеет работать с текстом, приводить в нач. форму слова и т.д.)

url = requests.get('https://pypi.org/project/types-aiobotocore-ecr-public/')

'''чтобы получить элемент веб-страницы из объекта бс, нужно вызвать метод select(), возвращающий объект Tag,
и передать ему строку CSS-селектора искомого элемента (напоминает регулярные выражения, но в HTML страницах)'''

'''Примеры CSS-селекторов soup.select('селектор'):
div, #author, .notice, div span, div>span, input[name], input[type='button']
!!! Селекторы могут сочетаться, образуя сложные шаблоны (p #author)

Скопировать нужный селектор можно в браузере, в консоли разработчика (правой кнопкой на код элемента -> копировать -> CSS-селектор)'''

def parser(value):
    try:
        url = requests.get(value)
        url.raise_for_status()  # метод остановит программу в случае неудачной загрузки
        with open('webfile.html', 'wb') as file:
            file.writelines(url)  # копируем html страницу целиком

        with open('webfile.html', 'rb') as file:  # заново открываем файл в режиме чтения
            bsfile = bs4.BeautifulSoup(file.read(), 'html.parser')# создаем объект бс
            elems = bsfile.select('#description > div')  # возвращаем нужный элемент по селектору (объект Tag)
            # а чтобы извлечь из объекта бс все элементы, в качестве селектора нужно передать 'p'
            # print(len(elems))# узнаем количество элементов (1)
            # print(elems[0].getText())# распечатываем его
            with open('text.txt', 'w', encoding='utf-8') as text_file:
                text_file.writelines(elems[0].getText())  # записываем спарсенное в новый файл

        return True

    except:
        return False

if __name__ == '__main__':
    raise Exception('Запущен модуль!')