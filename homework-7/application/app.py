import os
import threading
import settings
import requests

from flask import Flask, request, jsonify

app = Flask(__name__)

mock_host = settings.MOCK_HOST
mock_port = settings.MOCK_PORT

@app.route('/users/<name>', methods=['PUT'])
def change_user_id_by_name(name):
    try:
        data = request.json
        resp = requests.put(
            f'http://{mock_host}:{mock_port}/users/{name}',
            json=data
        )
        if resp.status_code == 200:
            res = resp.json()
            return jsonify(res), 200
        if resp.status_code == 404:
            return jsonify(f'User name {name} not found'), 404

    except Exception as e:
        print(f'Unable to update user data on external system:\n{e}')

@app.route('/users/<name>', methods=['GET'])
def get_user_id_by_name(name):
    try:
        resp = requests.get(f'http://{mock_host}:{mock_port}/users/{name}')

        if resp.status_code == 200:
            res = resp.json()
            return jsonify(res), 200
        if resp.status_code == 404:
            return jsonify(f'User name {name} not found'), 404

    except Exception as e:
        print(f'Unable to get surname from external system:\n{e}')


@app.route('/users/<name>', methods=['DELETE'])
def delete_user_id_by_name(name):
    try:
        resp = requests.delete(f'http://{mock_host}:{mock_port}/users/{name}')

        if resp.status_code == 200:
            res = resp.json()
            return jsonify(res), 200
        if resp.status_code == 404:
            return jsonify(f'User name {name} not found'), 404

    except Exception as e:
        print(f'Unable to update user data on external system:\n{e}')

# @app.route('/shutdown')
# def shutdown():
#     shutdown_stub()
#     return jsonify(f'Ok, exiting'), 200

# def shutdown_stub():
#     terminate_func = request.environ.get('werkzeug.server.shutdown')
#     if terminate_func:
#         terminate_func()


def run_app():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.APP_HOST,
        'port': settings.APP_PORT
    })

    server.start()
    return server

if __name__ == '__main__':
    app.run(os.environ.get('APP_HOST', '127.0.0.1'), os.environ.get('APP_PORT', '8080'))
