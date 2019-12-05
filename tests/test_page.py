import pytest
from pages.main_page import AutomationMainPage
from pages.search_page import AutomationSearchPage
from pages.contact_page import AutomationContactPage
from selenium.webdriver import Firefox


@pytest.fixture(scope="class")
def browser():
    driver = Firefox()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()


class TestContactPage:
    def test_sendContact_emptyEmailAddress_emptyEmailErrorShouldBeDisplayed(self, browser):
        """
        This test sends empty message in "Contact" page
        Expected result: empty email address error
        """
        contact_page = AutomationContactPage(browser)
        contact_page.load()
        contact_page.click_send()
        error_message = contact_page.get_error_message_list()
        assert "Invalid email address" in error_message

    def test_sendContact_emailAddressWithoutMessage_emptyMessageShouldBeDisplayed(self, browser):
        """
        This test sends filled email information, empty message in "Contact" page
        Expected result: blank message error
        """
        contact_page = AutomationContactPage(browser)
        contact_page.load()
        contact_page.enter_email("test@test.com")
        contact_page.click_send()
        error_message = contact_page.get_error_message_list()
        assert "The message cannot be blank" in error_message


class TestSearchResults:
    def test_search_testPhraseWithoutMatches_noResultsMessageShouldBeDisplayed(self, browser):
        """
        This test searches for test phrase that expects no matches
        Expected result: 'No Results were found for your search' message
        """
        phrase = "test1test"
        main_page = AutomationMainPage(browser)
        search_page = AutomationSearchPage(browser)
        main_page.load()
        main_page.search(phrase)
        search_result_text = search_page.get_empty_search_result_text()
        assert 'No results were found for your search "test1test"' in search_result_text

    def test_search_testPhraseWithoutMatches_zeroResultsHeaderShouldBeDisplayed(self, browser):
        """
        This test searches for test phrase that expects no matches
        Expected result: '0 results' displayed in result header
        """
        phrase = "test1test"
        main_page = AutomationMainPage(browser)
        search_page = AutomationSearchPage(browser)
        main_page.load()
        main_page.search(phrase)
        search_result_header_text = search_page.get_search_header_text()
        assert "0 results" in search_result_header_text

    def test_search_testPhraseWithMatches_searchItemCountShouldMatchHeaderInformation(self, browser):
        """
        This test searches for test phrase that expects matches.
        It searches for the last present element which ensures presence of previous elements.
        Expected result: search result element count matches search header information
        """
        phrase = "dress"
        main_page = AutomationMainPage(browser)
        search_page = AutomationSearchPage(browser)
        main_page.load()
        main_page.search(phrase)
        search_result_header_element_count = str(search_page.get_search_header_text())[0]
        assert search_page.find_last_element_of_search_result(search_result_header_element_count)

    def test_search_testPhraseWithMatches_searchItemCountIsntHigherThanHeaderInformation(self, browser):
        """
        This test searches for test phrase that expects matches.
        It searches for the (last present + 1) element which ensures no more than expected elements are present.
        Expected result: search result element count matches search header information
        """
        phrase = "dress"
        main_page = AutomationMainPage(browser)
        search_page = AutomationSearchPage(browser)
        main_page.load()
        main_page.search(phrase)
        search_result_header_element_count = str(search_page.get_search_header_text())[0]
        assert not search_page.find_last_element_of_search_result(str(int(search_result_header_element_count)+1))

    def test_search_testPhraseWithMatches_productCountMatchesHeaderInformation(self, browser):
        """
        This test searches for test phrase that expects matches
        Expected result: search result product count information (Showing 1 - X) matches search header information
        """
        phrase = "dress"
        main_page = AutomationMainPage(browser)
        search_page = AutomationSearchPage(browser)
        main_page.load()
        main_page.search(phrase)
        search_result_text = search_page.get_search_result_text()
        search_result_header_text = str(search_page.get_search_header_text())[0]
        expected_product_count_string = "Showing 1 - "+str(search_result_header_text)
        assert expected_product_count_string in search_result_text
