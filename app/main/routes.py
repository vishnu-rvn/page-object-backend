from flask_restful import Resource, Api
from flask import Blueprint, jsonify
from app import mongo
from app.config import DBConfig


api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)


class ObjectMapList(Resource):
    def get(self):
        results = []
        for res in mongo.db[DBConfig.COLLECTION_NAME].find({}):
            results.append({
                "name": res["name"],
                "selector": res["selector"],
                "selector_type": res["type"],
                "page": res["page"]
            })
        return jsonify(results)


class FindElement(Resource):
    pass


class TestCaseList(Resource):
    pass


api.add_resource(ObjectMapList, '/')