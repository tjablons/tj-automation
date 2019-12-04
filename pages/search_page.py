from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AutomationSearchPage:
    RESULT_FIELD = (By.XPATH, "//p[contains(@class,'alert alert-warning')]")
    RESULT_AMOUNT = (By.XPATH, "//span[@class='heading-counter']")
    SEARCH_RESULT_ELEMENT = (By.XPATH, "//ul[@class='product_list grid row']//div[@class='product-image-container']")
    SEARCH_RESULT_LAST_ELEMENT = (By.XPATH, "(//ul[@class='product_list grid row']"
                                            "//div[@class='product-image-container'])[7]")
    SEARCH_RESULT_PRODUCT_COUNT = (By.CLASS_NAME, "product-count")

    @classmethod
    def generate_xpath_for_nth_element_of_search_result(cls, el_id=""):
        xpath = "(//ul[@class='product_list grid row']//div[@class='product-image-container'])["+str(el_id)+"]"
        return (By.XPATH, xpath)

    def __init__(self, browser):
        self.browser = browser

    def get_empty_search_result_text(self):
        return self.browser.find_element(*self.RESULT_FIELD).text

    def get_search_header_text(self):
        return self.browser.find_element(*self.RESULT_AMOUNT).text

    def get_search_result_element_count(self):
        return len(self.browser.find_elements(*self.SEARCH_RESULT_ELEMENT))

    def find_last_element_of_search_result(self, element_id):
        return self.browser.find_element(*self.generate_xpath_for_nth_element_of_search_result(element_id))

    def get_search_result_text(self):
        return self.browser.find_element(*self.SEARCH_RESULT_PRODUCT_COUNT).text
