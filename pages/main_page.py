from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AutomationMainPage:
    """
    Class with selectors and methods for Home page
    """
    URL = "http://automationpractice.com/index.php"
    SEARCH_INPUT = (By.ID, "search_query_top")
    CONTACT_BUTTON = (By.LINK_TEXT, "Contact us")
    CART = (By.XPATH, "//div[@class='shopping_cart']/a[1]")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

    def click_contact(self):
        self.browser.find_element(*self.CONTACT_BUTTON).click()

    def click_cart(self):
        self.browser.find_element(*self.CART).click()
