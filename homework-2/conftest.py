from ui.fixtures import *

import os
import shutil
import pytest

def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://target.my.com/')

@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')

    return {'browser': browser, 'url': url}


@pytest.fixture(scope='session')
def base_temp_dir():

    base_dir = '/home/dashori/Рабочий стол/maiil/tests'

    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)

    os.makedirs(base_dir)
    return base_dir


@pytest.fixture(scope='function')
def temp_dir(base_temp_dir, request):
    test_dir = os.path.join(base_temp_dir, request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_'))
    os.makedirs(test_dir)
    return test_dir

