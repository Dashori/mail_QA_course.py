from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class,'responseHead-module-button')]")
    EMAIL_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'password')
    ENTER_LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")

class DashboardPageLocators:
    CAMPAIGS_LOCATOR = (By.XPATH, "//div[contains(@class, 'center-module-campaigns')]")
    AUDITORIUM_LOCATOR = (By.XPATH, "//a[contains(@href, '/segments')]")
    CREATE_CAMPAIGN_LOCATOR_1 = (By.XPATH, "//a[contains(@href, '/campaign/new')]")
    CREATE_CAMPAIGN_LOCATOR_2 = (By.XPATH, "//div[contains(@class, 'button-module-textWrapper')]")

class SegmentLocators:
    CREATE_NEW_SEGMENT_LOCATOR_1 =  (By.XPATH, "//a[contains(@href, '/segments/segments_list/new/')]")
    CREATE_NEW_SEGMENT_LOCATOR_2 = (By.XPATH, "//div[contains(@class, 'button__text')]")
    SEGMENT_SOURCE_LOCATOR = (By.XPATH,"//input[contains(@class, 'adding-segments-source__checkbox')]")
    ADD_SEGMENT_LOCATOR = (By.XPATH,"//div[contains(@class, 'adding-segments-modal__btn')]")
    TITLE_SEGMENT_INPUT_LOCATOR_2 = (By.XPATH,"//input[@class='input__inp')]")
    TITLE_SEGMENT_INPUT_LOCATOR_1 = (By.XPATH,"//div[@class='input input_create-segment-form'] //input")
    CREATE_SEGMENT_LOCATOR = (By.XPATH,"//button[contains(@class, 'button_submit')]")
    
    NEW_SEGMENT_LOCATOR = (By.XPATH, "//div[contains(@class, 'button__text')]")
    REMOVE_SEGMENT_LOCATOR = (By.XPATH,"//span[contains(@class, 'cells-module-removeCell')]")
    REMOVE_SEGMENT_OK_LOCATOR = (By.XPATH,"//button[contains(@class, 'button_confirm-remove')]")

    COUNT_SEGMENT_LOCATOR = (By.XPATH, "//span[contains(@class, 'pagination-module-pages']")

class CampaignLocators:
    
    СOVERAGE_TYPE_LOCATOR = (By.XPATH,"//div[contains(@class, 'column-list-item _reach')]")
    URL_LOCATOR = (By.XPATH,"//input[contains(@class, 'mainUrl-module-searchInput')]")
    TITLE_INPUT_LOCATOR = (By.XPATH,"//input[contains(@class, 'input__inp js-form-element')]")
    BANNER_LOCATOR = (By.ID,"patterns_banner_4")
    AUTO_LOCATOR = (By.XPATH,"//div[@class='group-module-item-39Dt4K']//span[@class='toggle-module-handler-1BTvgf']")
    
    IMAGE_INPUT_LOCATOR = (By.XPATH, '//input[@data-test="image_240x400"]')
    IMAGE_SUBMIT_LOCATOR = (By.XPATH,'//input[@type="submit"]')
    CREATE_CAMPAIGN_LOCATOR = (By.XPATH,"//div[contains(@class, 'js-save-button-wrap')]")