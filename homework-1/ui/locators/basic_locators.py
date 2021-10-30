from selenium.webdriver.common.by import By

LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class,'responseHead-module-button')]")
EMAIL_LOCATOR = (By.NAME, 'email')
PASSWORD_LOCATOR = (By.NAME, 'password')
ENTER_LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")

INFO_LOCATION = (By.XPATH, "//div[contains(@class, 'right-module-rightButton')]")
OUT_LOCATION = (By.XPATH, "//a[contains(@href, '/logout')]")

PROFILE_LOCATION = (By.XPATH, "//a[contains(@class, 'center-module-profile')]")
NAME_LOCATION = (By.XPATH, "//div[@data-name='fio']//input[@type='text']")
TELEPHONE_LOCATION = (By.XPATH, "//div[@data-name='phone']//input[@type='text']")
SAVE_INFO_LOCATION = (By.XPATH, "//div[@class='button__text']")

LOCATOR = lambda x: (By.XPATH, f"//a[contains(@class, 'center-module-{x}')]")
