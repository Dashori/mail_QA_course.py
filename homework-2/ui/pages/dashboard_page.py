from ui.locators.basic_locators import DashboardPageLocators
from ui.pages.base_page import BasePage
from ui.pages.segment_page import SegmentPage
from ui.pages.campaign_page import CampaignPage

from selenium.common.exceptions import TimeoutException


class DashboardPage(BasePage):

    url = 'https://target.my.com/'

    locators = DashboardPageLocators()

    def go_to_auditorium(self):
        self.click(self.locators.AUDITORIUM_LOCATOR)
        return SegmentPage(self.driver)

    def go_to_campaign(self):
        try:
            self.click(self.locators.CREATE_CAMPAIGN_LOCATOR_2)
        except TimeoutException:
            self.click(self.locators.CREATE_CAMPAIGN_LOCATOR_1)
        return CampaignPage(self.driver)
