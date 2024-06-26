from flask import Flask, render_template, request, redirect, abort, jsonify
from tools.text_translater import api_translator
from tools.dbmanager import ManagerDB
from flask_restful import Api, Resource
from main import main, creator
from random import randint


app = Flask(__name__.split('.')[0])
api = Api(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    if request.method == 'POST':
        try:
            url = request.form.get('message')
            main(url, ip_addr)
            return redirect('/translate')
        except TypeError:
            return redirect('/')

    return render_template('index.html')


@app.route('/translate', methods=['GET', 'POST'])
@app.route('/translate/', methods=['GET', 'POST'])
def translate():
    wordlist = []
    index = 0
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    session = creator(ip_addr)
    count = session.get_count()

    try:
        wordlist = session.get_data()
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
            session.delete_word_from_db(wordlist[index])
            count = session.get_count()

    return render_template('words.html', en_word=en_word, ru_word=ru_word, count=count)


@app.errorhandler(404)
def page_not_found(error):
    return f'''Error {error}
    <form action="/" align="center">
    <button>На главную</button>
</form>''', 404


@app.route('/api')
def get_api():
    return render_template('api.html')


class GetDataFromDate(Resource):
    def get(self, date):
        """
        Возвращает id, ip и запросы по дате.
        """
        if len(date) != 10:
            return jsonify({'sorry': ['no', 'data']}), 404
        data = ManagerDB.get_api_requests(date)

        return jsonify(data)


class GetUserUrl(Resource):
    def get(self, username):
        """
        Возвращает список запросов по юзернейму.
        """
        if len(username) == 0:
            return jsonify({'sorry': ['no', 'data']}), 404
        data = ManagerDB.get_user_url(username)

        return jsonify(data)


class TranslateText(Resource):
    def get(self):
        """
        Возвращает переведенный на русский текст.
        """
        text = request.args.get('text')
        return api_translator(text)

    def post(self):
        text = request.form.get('text')
        return api_translator(text)


api.add_resource(GetDataFromDate, '/api/v1.0/requests/<string:date>')
api.add_resource(GetUserUrl, '/api/v1.0/user_requests/<string:username>')
api.add_resource(TranslateText, '/api/v1.0/translate')


if __name__ == '__main__':
    app.run()
