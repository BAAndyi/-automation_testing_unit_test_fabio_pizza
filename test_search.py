import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_search(unittest.TestCase):
    SEARCH = (By.XPATH, "//div[@class='search-results']/div[@class='result']")
    CLICKSEARCH = (By.XPATH, '//*[@id="search_button_"]')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_search(self):
        self.chrome.find_element(*self.SEARCH).click()
        self.chrome.find_element(*self.CLICKSEARCH).click()
        assert Test_search, "No search results found"