from flask_restful import Resource
from flask import Blueprint, jsonify, request
from flask_restful import Api
from pymongo.errors import WriteError, DuplicateKeyError
from hashlib import sha1

object_bp = Blueprint('object_bp', __name__)

from server.app import mongo

api = Api(object_bp)


def form_validation(form):
    if all(form.values()) and form['selector-type'] != 'placeholder-item':
        return form
    else:
        raise NotImplementedError


class Object(Resource):
    def get(self):
        query = mongo.db.object_repo.find()
        return jsonify({
            'data': list(query)
        })

    def post(self):
        form = request.form
        hash_id = sha1(form['name'].encode('utf-8')).hexdigest()
        try:
            form_data = form_validation(form)
            mongo.db.object_repo.insert({
                '_id': hash_id,
                'name': form['name'],
                'selector': form['selector'],
                'page': form['page'],
                'selector_type': form['page']
            })
            return {
                'status': 'OK',
                'message': 'Object successfully inserted'
            }
        except NotImplementedError:
            return {
                'status': 'error',
                'message': 'Object insertion failed!'
            }
        except WriteError:
            return {
                'status': 'error',
                'message': 'Object insertion failed!'
            }
        except DuplicateKeyError:
            return {
                'status': 'error',
                'message': 'Element already exist'
            }

    def delete(self, id):
        try:
            item = mongo.db.object_repo.delete_one({'_id': id})
            return {
                'status': 'OK',
                'message': 'Element deleted successfully'
            }
        except Exception:
            return {
                'status': 'error',
                'message': 'Element not deleted'
            }

    def put(self):
        form = request.form
        name = form['name']
        try:
            mongo.db.object_repo.update_one(
                {
                    'name': name
                },
                {
                    'selector': form['selector'],
                    'page': form['page'],
                    'selector_type': form['page']
                }
            )
            return {
                'status': 'OK',
                'message': 'Element updated successfully'
            }
        except:
            return {
                'status': 'error',
                'message': 'Element not updated'
            }

api.add_resource(Object, '/', '/<int:id>')
