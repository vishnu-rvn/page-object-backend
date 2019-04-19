from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from app.config import Config

mongo = PyMongo()
cors = CORS()

resources = {
    r'*': {
        'origin': '*'
    }
}

def create_app():
    from app.main.routes import api_blueprint
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)
    cors.init_app(app)
    app.register_blueprint(api_blueprint)
    return app