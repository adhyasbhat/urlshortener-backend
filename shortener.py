import random
import string
from connection import DatabaseConnection

class URLShortener:
    def __init__(self):
        self.db_connection = DatabaseConnection()

    def generate_short_url(self, long_url):
        short_identifier = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        short_url = f"http://example.com/{short_identifier}"
        data = {
            'short_url': short_url,
            'long_url': long_url
        }
        self.db_connection.collection.insert_one(data)
        return short_url

    def get_long_url(self, short_url):
        document = self.db_connection.collection.find_one({'short_url': short_url})
        return document['long_url'] if document else None

    def close_connection(self):
        self.db_connection.close_connection()
