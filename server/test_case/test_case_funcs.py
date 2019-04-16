from flask_restful import Resource
from flask import Blueprint, jsonify, request
from flask_restful import Api

test_case_bp = Blueprint('test_case_bp', __name__)

from server.app import mongo

api = Api(test_case_bp)


class TestCase(Resource):
    def get(self):
        result = mongo.db.test_case.find({}, {'tc_id': 1, 'tc_name': 1})
        return {
            'result': [r for r in result]
        }

    def put(self, tc_id):
        return tc_id

    def post(self):
        data = request.json
        print(request)
        # curs = mongo.db.test_case.find({}, {'_id': 1}).sort([("_id", -1)]).limit(1)
        # latest_id = list(curs)[0]['_id']
        # mongo.db.test_case.insert({
        #     '_id': latest_id+1,
        #     'tc_id': tc_id,
        #     'tc_name': tc_name,
        #     'tc_steps': []
        # })

    def delete(self, _id):
        mongo.db.test_case.delete_many({
            '_id': _id
        })
        return 'Successfully deleted'


api.add_resource(TestCase, '/tc', '/tc/<_id>', '/tc/<tc_id>/<tc_name>')
