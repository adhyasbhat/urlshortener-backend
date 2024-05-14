from flask import Flask, request, redirect
from shortener import URLShortener

app = Flask(__name__)
shortener = URLShortener()

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['long_url']
    short_url = shortener.generate_short_url(long_url)
    return short_url

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = shortener.get_long_url(short_url)
    if long_url:
        return redirect(long_url, code=302)
    else:
        return "Short URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
