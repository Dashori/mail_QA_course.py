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

    def test_logout(self):
        self.login(LOGIN, PASSWORD)
        self.logout()
        assert self.driver.current_url.startswith(INITIAL_URL)
    
    def test_profile(self):
        self.login(LOGIN, PASSWORD)
        self.profile(NAME, TELEPHONE)
        self.driver.refresh()
        assert NAME ==  self.find(basic_locators.NAME_LOCATION).get_attribute("value")
        assert TELEPHONE == self.find(basic_locators.TELEPHONE_LOCATION).get_attribute("value")
   
    @pytest.mark.parametrize(
        "menu_location, url",
        [
            pytest.param(
                basic_locators.LOCATOR('statistics'), STATISTIC_URL
            ),
            pytest.param(
                basic_locators.LOCATOR('pro'), PRO_URL
            )
        ]
    )
    def test_menu(self, menu_location, url):
        self.login(LOGIN, PASSWORD)
        self.click(menu_location)
        assert self.driver.current_url.startswith(url)
    
    