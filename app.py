from flask import Flask, render_template, request, redirect
from parsers import textparser, words_from_text, translator

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    url = ''
    if request.method == 'POST':
        url = request.form.get('message')

        textparser.parser(url)
        return redirect('/translate')


    return render_template('index.html', message=url)

@app.route('/translate', methods=['GET', 'POST'])
@app.route('/translate/', methods=['GET', 'POST'])
def translate():
    render_template('words.html')



if __name__ == '__main__':
    app.run(debug=True)