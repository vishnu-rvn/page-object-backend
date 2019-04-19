import os


class Config:
    MONGO_URI = "mongodb://localhost:27017/test_database"


class DBConfig:
    DB_NAME = "test_database"
    COLLECTION_NAME = "test_collection"