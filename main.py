import random
from tkinter import *
from tkinter import ttk

def main():

    #textparser.parser()
    #words_from_text.search()
    #translator.en_ru_translator()

    with open('en_ru_file.txt', 'r', encoding='UTF-8') as file:
        wordlist = []
        for line in file.readlines():
            wordlist.append(line)

    def click():
        '''Функция отрабатывает по клику кнопки'''
        words = random.choice(wordlist).split()
        lbl.config(text=f'{words[0]}')
        lbl2.config(text=f'{words[1]}')

    root = Tk()  # Создаем объект "окно"
    root.title('TakeWords')  # Заголовок окна
    root.geometry('640x480')  # Разрешение окна

    lbl = Label(text='En', font=("Arial Bold", 50))  # Метка
    lbl2 = Label(text='Ru', font=("Arial Bold", 20))  # Метка
    lbl.pack()  # Метка в окне
    lbl2.pack()  # Метка в окне


    button = ttk.Button(text='Далее', command=click())
    button.pack()

    root.mainloop()




if __name__ == '__main__':
    main()

