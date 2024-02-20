import requests, bs4
from parsers import words_from_text

#  nltk - модуль на будущее (умеет работать с текстом, приводить в нач. форму слова и т.д.)

standart_url = 'https://pypi.org/project/types-aiobotocore-ecr-public/'

def parser(value):
    try:
        url = requests.get(value)
        url.raise_for_status()
        with open('webfile.html', 'wb') as file:
            file.writelines(url)
            print('1 Ok')

        with open('webfile.html', 'rb') as file:
            bsfile = bs4.BeautifulSoup(file.read(), 'html.parser')
            elems = bsfile.select('#description > div')
            with open('text.txt', 'w', encoding='utf-8') as text_file:
                text_file.writelines(elems[0].getText())
                print('2 Ok')

        words_from_text.search()

    except:
        print('Попытка 2')
        parser(standart_url)

if __name__ == '__main__':
    raise Exception('Запущен модуль!')