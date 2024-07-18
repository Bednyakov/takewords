from tools.text_translater import api_translator
from tools.dbmanager import ManagerDB
from flask_restful import Resource
from flask import jsonify, request
from tasks import get_words_task
from app import api


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

        # Запускаем задачу асинхронно
        task = get_words_task.apply_async(args=[url, ip_addr])

        result = task.wait(timeout=10)

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
    


api.add_resource(GetWords, '/api/v1.0/words')
api.add_resource(GetDataFromDate, '/api/v1.0/requests/<string:date>')
api.add_resource(GetUserUrl, '/api/v1.0/user_requests/<string:username>')
api.add_resource(TranslateText, '/api/v1.0/translate')