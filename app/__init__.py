from flask import Flask
from flask_restful import Api
from .routes import init_routes
from .resources import init_resources

def create_app():

    app = Flask(__name__.split('.')[0])
    init_routes(app)

    api = Api(app)
    init_resources(api)

    return app