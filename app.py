from flask import Flask, request
import webbrowser
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def open_link():
    # A felhasználó által megadott URL
    url = request.args.get('url')  # URL paraméter a GET kérésben
    if url:
        # A webbrowser modul segítségével megnyitjuk a linket
        webbrowser.open(url)
        return f"Link opened in browser: {url}"
    else:
        return "No URL provided", 400  # Ha nincs URL paraméter

if __name__ == '__main__':
    app.run(debug=True, port=5000)