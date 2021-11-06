from ui.pages.base_page import BasePage
from ui.locators.basic_locators import CampaignLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

import os


class CampaignPage(BasePage):
    
    url = 'https://target.my.com/'

    locators = CampaignLocators()

    def add_campaign(self, campaign_name):
        target_url = 'lamoda.ru'
        image_path = os.path.join(os.path.dirname(__file__), 'photo.png')

        self.click(self.locators.СOVERAGE_TYPE_LOCATOR)
        self.send_element(self.locators.URL_LOCATOR, target_url)
        self.send_element(self.locators.TITLE_INPUT_LOCATOR, campaign_name, True)
        self.click(self.locators.BANNER_LOCATOR)
        self.click(self.locators.AUTO_LOCATOR)
        self.find_presence(self.locators.IMAGE_INPUT_LOCATOR).send_keys(image_path)
        self.click(self.locators.IMAGE_SUBMIT_LOCATOR)
        self.click(self.locators.CREATE_CAMPAIGN_LOCATOR)

    def is_campaign_exists(self, campaign_name):
        xpath = f'//a[@title="{campaign_name}"]'
        try:
            self.find((By.XPATH, xpath))
            return True
        except TimeoutException:
            return False
