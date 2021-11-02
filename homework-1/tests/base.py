import pytest
from ui.locators import basic_locators
import time
from data import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec


class BaseCase:

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def wait(self, delay=None):
        if delay is None:
            delay = 60
        return WebDriverWait(self.driver, timeout=delay)

    def find(self, locator, delay=50):
        return self.wait(delay).until(ec.visibility_of_element_located(locator))


    def send_element(self, locator: tuple, query: str, is_clear: bool = False):
        element = self.find(locator)
        if is_clear:
            element.clear()
        element.send_keys(query)

    def click(self, locator, delay=60):
        CLICK_RETRY = 5
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator,delay=delay)
                elem = self.wait(delay).until(ec.element_to_be_clickable(locator))
                elem.click()
                return
            except StaleElementReferenceException or TimeoutException:
                if i == CLICK_RETRY-1:
                    raise

    def login(self, log, passw):
        self.click(basic_locators.LOGIN_LOCATOR)
        self.send_element(basic_locators.EMAIL_LOCATOR, log)
        self.send_element(basic_locators.PASSWORD_LOCATOR, passw)
        self.click(basic_locators.ENTER_LOGIN_LOCATOR)

    def logout(self):
        self.click(basic_locators.INFO_LOCATION)
        self.click(basic_locators.OUT_LOCATION)

    def profile(self, name, teleph):
        self.click(basic_locators.PROFILE_LOCATION)
        self.send_element(basic_locators.NAME_LOCATION, name, True)
        self.send_element(basic_locators.TELEPHONE_LOCATION, teleph, True)
        self.click(basic_locators.SAVE_INFO_LOCATION)
