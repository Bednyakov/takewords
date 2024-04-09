from flask import Flask, render_template, request, redirect
from tools.dbmanager import get_data, delete_word_from_db
from random import randint
from main import main


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            url = request.form.get('message')
            main(url)
            return redirect('/translate')
        except TypeError:
            return redirect('/')

    return render_template('index.html')

@app.route('/translate', methods=['GET', 'POST'])
@app.route('/translate/', methods=['GET', 'POST'])
def translate():
    wordlist = []
    index = 0

    try:
        wordlist = get_data()
        if len(wordlist) == 0:
            return redirect('/')

        index = randint(0, len(wordlist) - 1)
        en_word = wordlist[index].split()[0]
        ru_word = wordlist[index].split()[1]

    except:
        en_word = 'Упс...'
        ru_word = 'Словарь не создан.'

    if request.method == 'POST':
        value = request.form.get('delete')
        if value:
            delete_word_from_db(wordlist[index])
            return render_template('words.html', en_word=en_word, ru_word=ru_word)

        return render_template('words.html', en_word=en_word, ru_word=ru_word)
    return render_template('words.html', en_word=en_word, ru_word=ru_word)



if __name__ == '__main__':
    app.run(debug=True)