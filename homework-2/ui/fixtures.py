import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from tests.data import *

from ui.pages.base_page import BasePage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.login_page import LoginPage
from ui.pages.segment_page import SegmentPage
from ui.pages.campaign_page import CampaignPage

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture
def dashboard_page(driver):
    return DashboardPage(driver=driver)

@pytest.fixture
def segment_page(driver):
    return SegmentPage(driver=driver)

@pytest.fixture
def campaign_page(driver):
    return CampaignPage(driver=driver)


def get_driver(browser_name, download_dir=None):
    if browser_name == 'chrome':
        options = Options()
        if download_dir is not None:
            options.add_experimental_option("prefs", {"download.default_directory": download_dir})

        manager = ChromeDriverManager(version='latest')
        browser = webdriver.Chrome(executable_path=manager.install(), options=options)
    else:
        raise RuntimeError(f'Unsupported browser: {browser_name}')

    browser.maximize_window()
    return browser

@pytest.fixture(scope='function')
def driver(config, temp_dir):
    url = config['url']
    
    browser = get_driver('chrome', download_dir=temp_dir)
    browser.get(url)

    yield browser
    browser.quit()

@pytest.fixture(scope='session')
def credentials():

    user = EMAIL
    password = PASS

    return user, password

@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver('chrome')
    driver.get(config['url'])
    
    login_page = LoginPage(driver)
    login_page.login(*credentials)

    cookies = driver.get_cookies()
    driver.quit()
    return cookies

