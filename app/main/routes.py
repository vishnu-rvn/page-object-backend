from flask_restful import Resource, Api
from flask import Blueprint, jsonify
from app import mongo
from app.config import DBConfig
from selenium import webdriver
from driver_engine.init_driver import InitDriver


api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)
init_driver = InitDriver()


class LaunchDriver(Resource):
    def get(self):
        init_driver.create_driver()
        return "Driver Launched"


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
    def get(self):
        try:
            init_driver.driver.get("http://www.google.com")
        except AttributeError:
            return "error"

class TestCaseList(Resource):
    pass


api.add_resource(ObjectMapList, '/')
api.add_resource(FindElement, '/find_element')
api.add_resource(LaunchDriver, '/launch_driver')