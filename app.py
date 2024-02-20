from flask import Flask, render_template, request, redirect
from parsers import textparser
from random import randint

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    url = ''
    if request.method == 'POST':
        url = request.form.get('message')

        textparser.parser(url)
        return redirect('/translate')


    return render_template('index.html', message=url)

@app.route('/translate')
@app.route('/translate/')
def translate():
    with open('en_ru_file.txt', 'r', encoding='UTF-8') as file:
        wordlist = []
        for line in file.readlines():
            wordlist.append(line)
        index = randint(0, len(wordlist) - 1)
    return render_template('words.html', words=wordlist[index])



if __name__ == '__main__':
    app.run(debug=True)