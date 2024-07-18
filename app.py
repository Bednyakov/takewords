from flask import Flask
from flask_restful import Api
from celery_worker import make_celery


def create_app():
    app = Flask(__name__.split('.')[0])
    app.config.update(
        broker_url = 'redis://localhost:6379/0',
        result_backend = 'redis://localhost:6379/0'
    )
    return app


app = create_app()
celery = make_celery(app)
api = Api(app)


if __name__ == '__main__':
    app.run()