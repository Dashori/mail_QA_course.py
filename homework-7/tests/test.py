import json
import settings
from application.app import run_app
from client import Client

def test_first_test():
    run_app()    

def test_mock_down():
    host, port = settings.APP_HOST, settings.APP_PORT
    run_app()

    client = Client(host=host, port=port)
    response = client.request('/users/Arisha', 'GET')
    
    client.request('/shutdown', 'GET')

    assert response['status_code'] == 500


def test_get_user(socket_client):
    response = socket_client.request('/users/Dasha', 'GET')
    body = json.loads(response['body'])

    assert response['status_code'] == 200
    assert body['surname'] == 'Chepigo'


def test_get_not_exist_user(socket_client):
    response = socket_client.request('/users/Fedya', 'GET')

    assert response['status_code'] == 404


def test_update_user_age(socket_client):
    data = {
        'surname': 'Chepigo',
        'age': 20
    }
    headers = {'Content-Type': 'application/json'}
    response = socket_client.request(
        '/users/Dasha',
        'PUT',
        headers=headers,
        data=data
    )
    body = json.loads(response['body'])

    assert response['status_code'] == 200
    assert body['age'] == 20


def test_delete_user(socket_client):

    response_delete = socket_client.request('/users/Dasha', 'DELETE')
    body_delete = json.loads(response_delete['body'])

    response_get = socket_client.request('/users/Dasha', 'GET')
    body_get = json.loads(response_get['body'])

    assert response_delete['status_code'] == 200
    assert body_delete['deleted']
    assert body_get == 'User name Dasha not found'


def test_delete_not_exist_user(socket_client):
    response_delete = socket_client.request('/users/Arisha', 'DELETE')

    assert response_delete['status_code'] == 404
