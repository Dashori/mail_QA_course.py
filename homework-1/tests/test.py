from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time
from base import BaseCase
from ui.locators import basic_locators
from data import *
import pytest

@pytest.mark.UI
class TestOne(BaseCase):

    def test_login(self):
        self.login(LOGIN, PASSWORD)
        assert self.driver.current_url == DASHBOARD_URL

    def test_badlogin(self):
        self.login(LOGIN, BAD_PASSWORD)
        assert self.driver.current_url != DASHBOARD_URL
    
    def test_logut(self):
        self.login(LOGIN, PASSWORD)
        self.logout()
        assert self.driver.current_url == INITIAL_URL

    @pytest.mark.parametrize(
        "menu_location, url", 
        [
            pytest.param(
                basic_locators.STATISTIC_LOCATION, STATISTIC_URL
            ),
            pytest.param(
                basic_locators.PRO_LOCATION, PRO_URL
            )
        ]
    )
    def test_menu(self, menu_location, url):
        self.login(LOGIN, PASSWORD)
        self.click(menu_location)
        time.sleep(3)
        assert self.driver.current_url == url
    