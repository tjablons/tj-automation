from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AutomationContactPage:
    """
    Class with selectors and methods for Contact Page
    """
    URL = "http://automationpractice.com/index.php?controller=contact"
    SEND_BUTTON = (By.XPATH, "//span[contains(text(),'Send')]")
    EMAIL_ADDRESS_INPUT = (By.ID, "email")
    ERROR_MESSAGE_ELEMENT = (By.XPATH, "//div[@class='alert alert-danger']")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def click_send(self):
        self.browser.find_element(*self.SEND_BUTTON).click()

    def get_error_message_list(self):
        return self.browser.find_element(*self.ERROR_MESSAGE_ELEMENT).text

    def enter_email(self, email):
        email_input = self.browser.find_element(*self.EMAIL_ADDRESS_INPUT)
        email_input.send_keys(email + Keys.RETURN)
