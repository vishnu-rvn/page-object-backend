from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import sys

sys.path.append('/home/vishnu/MyProject/pom/framework')


resources = {
    r'*': {
        'origin': '*'
    }
}
app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(os.path.dirname(
    os.path.dirname(BASE_DIR)), 'server_ui\\src\\media')
ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png', 'JPG'}

app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'true'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mongo = PyMongo(app)
api = Api(app)
cors = CORS(app, resources=resources)

from server.object_page.object_funcs import object_bp
from server.test_case.test_case_funcs import test_case_bp

app.register_blueprint(object_bp)
app.register_blueprint(test_case_bp)

if __name__ == '__main__':
    app.run(debug=True)
