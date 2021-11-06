from ui.pages.base_page import BasePage
from ui.pages.dashboard_page import DashboardPage


class LoginPage(BasePage):

    def login(self, log, passw):
        self.click(self.locators.LOGIN_LOCATOR)
        self.send_element(self.locators.EMAIL_LOCATOR, log)
        self.send_element(self.locators.PASSWORD_LOCATOR, passw)
        self.click(self.locators.ENTER_LOGIN_LOCATOR)
        return DashboardPage(self.driver)

    
    