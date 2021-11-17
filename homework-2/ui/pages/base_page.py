from ui.locators.basic_locators import BasePageLocators
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


CLICK_RETRY = 3

class BasePage():

    locators = BasePageLocators
    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, delay=None):
        try:
            return self.wait(delay).until(ec.element_to_be_clickable(locator))
        except TimeoutException:
            return self.wait(delay).until(ec.presence_of_element_located(locator))

    def send_element(self, locator: tuple, query: str, is_clear: bool = False):
        element = self.find(locator)
        if is_clear:
            element.clear()
        element.send_keys(query)

    def click(self, locator, delay=10):
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator,delay=delay)
                elem = self.wait(delay).until(ec.element_to_be_clickable(locator))
                elem.click()
                return
            except StaleElementReferenceException or TimeoutException:
                if i == CLICK_RETRY-1:
                    raise
            