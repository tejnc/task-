from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/check/<string:email>')
def check_info(email):
    return "received"

if __name__ == "__main__":
    app.run(debug=True)