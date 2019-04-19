from pymongo import MongoClient
import dns
import json

client = MongoClient("mongodb://localhost:27017")

def inject_dummy_data():
    db = client.test_database
    if 'test_collection' in db.list_collection_names():
        print('data present')
    else:
        collection = db.test_collection
        with open('dataApr-19-2019.json', 'r') as file:
            contents = json.load(file)
        for item in contents:
            collection.insert_one(item)


if __name__ == "__main__":
    inject_dummy_data()