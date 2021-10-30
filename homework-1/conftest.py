import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://target.my.com')


@pytest.fixture()
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')

    return {'browser': browser, 'url': url}


@pytest.fixture(scope="function")
def driver(config):

    browser = config['browser']
    url = config['url']

    if browser == 'chrome':
        browser = webdriver.Chrome(executable_path='C:/Users/Даша/Desktop/mail/maiil/maiil/chromedriver.exe')
    else:
        raise RuntimeError(f'Unsupported browser: {browser}')

    browser.get(url)

    browser.maximize_window()
    browser.set_network_conditions(
        offline=False,
        latency=5,
        download_throughput=1024 * 1024,
        upload_throughput=1024 * 1024
    )
    yield browser
    browser.close()
