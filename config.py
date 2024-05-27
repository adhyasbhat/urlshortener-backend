from pymongo import MongoClient

class Config:
    MONGODB_URI = 'mongodb://localhost:27017/'
    DATABASE_NAME = 'short_urls'

def get_database():
    client = MongoClient(Config.MONGODB_URI)
    return client[Config.DATABASE_NAME]
