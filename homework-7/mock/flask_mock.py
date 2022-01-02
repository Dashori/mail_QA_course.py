import threading
from flask import Flask, jsonify, request
from settings import DICT, MOCK_HOST, MOCK_PORT

app = Flask(__name__)

@app.route('/users/<name>', methods=['GET'])
def get_user_surname(name):
    if data := DICT.get(name):
        return {"surname": data['surname']}, 200
    else:
        return jsonify(f'Surname for user {name} not fount'), 404


@app.route('/users/<name>', methods=['PUT'])
def update_user_surname(name):
    if data := DICT.get(name):
        request_data = request.json
        data['surname'] = request_data['surname']
        data['age'] = request_data['age']
        DICT[name] = data
        return jsonify(data), 200
    else:
        return jsonify(f'User {name} not fount'), 404


@app.route('/users/<name>', methods=['DELETE'])
def delete_task(name):
    if DICT.get(name):
        del DICT[name]
        return jsonify({'deleted': True}), 200
    else:
        return jsonify(f'User {name} not fount'), 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': MOCK_HOST,
        'port': MOCK_PORT
    })
    server.start()
    return server
