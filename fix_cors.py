from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Allow all origins for testing

if __name__ == '__main__':
    app.run(debug=True, port=5000)