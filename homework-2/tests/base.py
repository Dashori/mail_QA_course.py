import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.login_page import LoginPage

CLICK_RETRY = 3

class BaseCase:

    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page =  BasePage(driver)
        self.dashboard_page = DashboardPage(driver)
        self.login_page = LoginPage(driver)
        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)

            self.driver.refresh()
            self.dashboard_page = DashboardPage(driver)

        

   
  