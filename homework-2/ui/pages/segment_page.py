from ui.pages.base_page import BasePage
from ui.locators.basic_locators import SegmentLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class SegmentPage(BasePage):
    locators = SegmentLocators

    def add_segment(self, segment_name):
        try:
            self.click(self.locators.CREATE_NEW_SEGMENT_LOCATOR_1)
        except TimeoutException:
            self.click(self.locators.CREATE_NEW_SEGMENT_LOCATOR_2)

        self.click(self.locators.SEGMENT_SOURCE_LOCATOR)
        self.click(self.locators.ADD_SEGMENT_LOCATOR)
        try:
            title = self.find(self.locators.TITLE_SEGMENT_INPUT_LOCATOR_1, delay = 10)
        except TimeoutException:
            title = self.find(self.locators.TITLE_SEGMENT_INPUT_LOCATOR_2, delay = 10)
        
        title.click()
        self.send_element(title, segment_name, True)
        self.click(self.locators.CREATE_SEGMENT_LOCATOR)

    def new_segment(self, segment_name):
        path = f'//a[@title = "{segment_name}"]'
        try:
            self.find((By.XPATH, path))
            return True
        except TimeoutException:
            return False

    def remove_segment(self):
        self.click(self.locators.REMOVE_SEGMENT_LOCATOR)
        self.click(self.locators.REMOVE_SEGMENT_OK_LOCATOR)
    