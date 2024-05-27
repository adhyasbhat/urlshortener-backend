from pyshorteners import Shortener
from config import get_database

def shorten_url(long_url,url_name):
    # Initialize the shortener (using TinyURL)
    shortener = Shortener()
    # Shorten the URL
    short_url = shortener.tinyurl.short(long_url)
    
    # Save the original and shortened URLs in MongoDB
    database = get_database()
    collection = database['urls']
    collection.insert_one({'url_name': url_name, 'short_url': short_url})
    
    return short_url
