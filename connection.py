from pymongo import MongoClient

class DatabaseConnection:
    def __init__(self, host='localhost', port=27017, database_name='url', collection_name='urlDetails'):
        self.client = MongoClient(f'mongodb://{host}:{port}/')
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def close_connection(self):
        self.client.close()
