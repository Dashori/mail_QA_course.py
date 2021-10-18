from _pytest.mark import deselect_by_mark
import pytest
from ui.locators import basic_locators
import selenium
import time 
from data import *
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import ElementNotInteractableException, StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

CLICK_RETRY = 3

class BaseCase:

    driver = None
    
    @pytest.fixture(scope = 'function', autouse = True)
    def setup(self, driver):
        self.driver = driver

    def find(self, locator):
        delay = 60
        element = wait(self.driver, delay).until(ec.presence_of_element_located(locator))
        if 1:
            return element
        else:
            return wait(self.driver, delay).until(ec.visibility_of_element_located(locator))

    def login_email(self, elem, query):
        email = self.find(elem)
        email.send_keys(query)
        time.sleep(2)

    def login_password(self, elem, query) :   
        password = self.find(elem)
        password.send_keys(query)
        time.sleep(2)

    def telephone(self, elem, query):
        telephone = self.find(elem)
        telephone.clear()
        telephone.send_keys(query)
    
    def name(self, elem, query):
        name = self.find(elem)
        name.clear()
        name.send_keys(query)


    def click(self, locator):
        try:
            self.find(locator).click()
        except TimeoutException:
            self.find(locator).click()

    def login(self, log, passw):
        self.click(basic_locators.LOGIN_LOCATOR)
        self.login_email(basic_locators.EMAIL_LOCATOR, log)
        self.login_password(basic_locators.PASSWORD_LOCATOR, passw)
        self.click(basic_locators.ENTER_LOGIN_LOCATOR)

    def logout(self):
        time.sleep(5)
        self.click(basic_locators.INFO_LOCATION)
        time.sleep(5)
        self.click(basic_locators.OUT_LOCATION)
    
    def profile(self, name, teleph):
        self.click(basic_locators.PROFILE_LOCATION)
        self.name(basic_locators.NAME_LOCATION, name)
        self.telephone(basic_locators.TELEPHONE_LOCATION, teleph)
        self.click(basic_locators.SAVE_INFO_LOCATION)
    