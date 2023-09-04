from flask import Flask, jsonify

app = Flask(__name__)


def checker(data):
    return "heheh"


@app.route('/page', methods=['GET'])
def new():
    name = False
    if name is True:
        checker("hehehe")

    return jsonify({
        'name': 'Dhruv'
    })