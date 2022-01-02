import os
import pytest
import settings
from application.app import run_app
from client import Client
from mock import flask_mock

repo_root = os.path.abspath(os.path.join(__file__, os.pardir))

@pytest.fixture(scope='session')
def run():
    flask_mock.run_mock()
    run_app()
    yield
    client_mock = Client(settings.MOCK_HOST, settings.MOCK_PORT)
    client_app = Client(settings.APP_HOST, settings.APP_PORT)

    client_app.request(method="GET", url="/shutdown")
    try:
        client_mock.request(method="GET", url="/shutdown")
    except:
        pass


@pytest.fixture(scope='function')
def socket_client(run):
    client = Client(port=settings.APP_PORT, host=settings.APP_HOST)
    return client
