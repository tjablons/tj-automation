import pytest
from pages.main_page import AutomationMainPage
from pages.search_page import AutomationSearchPage
from pages.contact_page import AutomationContactPage
from selenium.webdriver import Firefox
import time


@pytest.fixture(scope="class")
def browser():
    driver = Firefox()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()


class TestContactPage:
    def test_send_empty_email(self, browser):
        contact_page = AutomationContactPage(browser)
        contact_page.load()
        contact_page.click_send()
        error_message = contact_page.get_error_message_list()
        assert "Invalid email address" in error_message

    def test_send_email_with_empty_message(self, browser):
        contact_page = AutomationContactPage(browser)
        contact_page.load()
        contact_page.enter_email("test@test.com")
        error_message = contact_page.get_error_message_list()
        assert "The message cannot be blank" in error_message


class TestSearchResults:
    def test_search_no_matches_elements(self, browser):
        phrase = "test1"
        main_page = AutomationMainPage(browser)
        search_page = AutomationSearchPage(browser)
        main_page.load()
        main_page.search(phrase)
        search_result_text = search_page.get_empty_search_result_text()
        assert search_result_text == 'No results were found for your search "test1"'

    def test_search_no_matches_header(self, browser):
        phrase = "test1"
        main_page = AutomationMainPage(browser)
        search_page = AutomationSearchPage(browser)
        main_page.load()
        main_page.search(phrase)
        search_result_header_text = search_page.get_search_header_text()
        assert "0 results" in search_result_header_text

    def test_search_with_matches_elements(self, browser):
        phrase = "dress"
        main_page = AutomationMainPage(browser)
        search_page = AutomationSearchPage(browser)
        main_page.load()
        main_page.search(phrase)
        assert search_page.find_last_element_of_search_result(7) == 1

    def test_search_with_matches_header(self, browser):
        phrase = "dress"
        main_page = AutomationMainPage(browser)
        search_page = AutomationSearchPage(browser)
        main_page.load()
        main_page.search(phrase)
        search_result_header_text = search_page.get_search_header_text()
        assert "7 results" in search_result_header_text

    def test_search_with_matches_text(self, browser):
        phrase = "dress"
        main_page = AutomationMainPage(browser)
        search_page = AutomationSearchPage(browser)
        main_page.load()
        main_page.search(phrase)
        search_result_text = search_page.get_search_result_text()
        assert "Showing 1 - 7" in search_result_text