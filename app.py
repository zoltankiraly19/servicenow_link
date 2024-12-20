from flask import Flask, request, redirect
from flask_cors import CORS  # CORS importálása

app = Flask(__name__)
# CORS engedélyezése a frontend domain-re
CORS(app, resources={r"/*": {"origins": "https://serviclink.1f0o357viivn.us-south.codeengine.appdomain.cloud"}})

@app.route('/', methods=['GET'])
def open_link():
    url = request.args.get('url')
    if url:
        # HTTP átirányítás a megadott URL-re
        return redirect(url, code=302)
    else:
        return "No URL provided", 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
