from flask import Flask, render_template, request, redirect
from parsers import textparser
from random import randint
from main import main


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('message')
        main(url)
        return redirect('/translate')

    return render_template('index.html')

@app.route('/translate', methods=['GET', 'POST'])
@app.route('/translate/', methods=['GET', 'POST'])
def translate():

    try:
        with open('en_ru_file.txt', 'r', encoding='UTF-8') as file:
            wordlist = []
            for line in file.readlines():
                wordlist.append(line)
            index = randint(0, len(wordlist) - 1)
            en_word = wordlist[index].split()[0]
            ru_word = wordlist[index].split()[1]

    except:
        en_word = 'Упс...'
        ru_word = 'Словарь не создан.'

    if request.method == 'POST':
        return render_template('words.html', en_word=en_word, ru_word=ru_word)
    return render_template('words.html', en_word=en_word, ru_word=ru_word)



if __name__ == '__main__':
    app.run(debug=True)