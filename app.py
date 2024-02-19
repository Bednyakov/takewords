from flask import Flask, render_template, request
from parsers import textparser, words_from_text, translator

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    #print(request.form['message'])
    print(request.form.get('message'))
    if request.method == 'POST':
        url = request.form.get('message')

    if textparser.parser(url) != False:
        words_from_text.search()
        print('Выполняется перевод. Это может занять пару минут.')
        translator.en_ru_translator()
        print('Перевод завершен!')
        render_template('words.html')

    return render_template('index.html', message='client_message')



if __name__ == '__main__':
    app.run(debug=True)