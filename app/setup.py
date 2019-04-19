import pymongo
from pymongo.errors import CollectionInvalid

client = pymongo.MongoClient("mongodb://localhost:27017")


def setup_db(db_name, collection_name):
    if db_name in client.list_database_names():
        print('Database: {} already present'.format(db_name))
        db = client['db_name']
        try:
            db.create_collection(collection_name)
        except CollectionInvalid:
            print('Collection: {} already exists'.format(collection_name))
    else:
        db = client[db_name]
        db.create_collection(collection_name)