from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/page', methods=['GET'])
def new():
    print("hehe")
    return "Working"