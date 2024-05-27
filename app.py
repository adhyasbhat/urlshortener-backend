from flask import Flask, request, jsonify
from flask_cors import CORS
from shorten import shorten_url
from config import get_database

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/shorten', methods=['POST'])
def shorten_endpoint():
    long_url = request.json.get('long_url')
    url_name = request.json.get('url_name')
    print(long_url)
    
    # Shorten the URL
    short_url = shorten_url(long_url, url_name)
    
    return jsonify({'short_url': short_url, 'url_name': url_name})

@app.route('/urls', methods=['GET'])
def get_urls():
    database = get_database()
    collection = database['urls']
    urls = list(collection.find({}, {'_id': 0}))  # Fetch all URLs and exclude the MongoDB _id field
    return jsonify(urls)

if __name__ == '__main__':
    app.run(debug=True)
