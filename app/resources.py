from tools.text_translater import api_translator
from tools.dbmanager import ManagerDB
from flask import jsonify, request
from flask_restful import Resource
from app.main import main, creator


class GetWords(Resource):
    def get(self) -> dict:
        """
        Возвращает en-ru словарь из страницы по url.
        """
        url = request.args.get('url')
        if not url:
            return {'error': 'URL parameter is required'}, 400

        # Получаем IP-адрес из заголовков
        ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)

        main(url, ip_addr)
        session = creator(ip_addr)
        wordlist: list = session.get_data()

        result = {item.split()[0]: item.split()[1] for item in wordlist if len(item.split()) >= 2}

        return jsonify(result)


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
        ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
        result = api_translator(text, ip_addr)
        return jsonify({'translate': result})

    def post(self):
        text = request.form.get('text')
        ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
        result = api_translator(text, ip_addr)
        return jsonify({'translate': result})



def init_resources(api):
    api.add_resource(GetWords, '/api/v1.0/words')
    api.add_resource(GetDataFromDate, '/api/v1.0/requests/<string:date>')
    api.add_resource(GetUserUrl, '/api/v1.0/user_requests/<string:username>')
    api.add_resource(TranslateText, '/api/v1.0/translate')