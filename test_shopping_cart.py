import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_shopping(unittest.TestCase):
    SELECT_PIZZA = (By.XPATH, "//a[@href='https://www.fabiopizza.ro/Pizza' and text()='Pizza']")
    FILTRU_NU_CARNE = (By.XPATH, "//button[@class='searchtag tag-vegy js-searchtag']")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro/")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_filtru_nu_carne(self):
       self.chrome.find_element(*self.SELECT_PIZZA).click()
       self.chrome.find_element(*self.FILTRU_NU_CARNE).click()
       assert Test_shopping, "Non-meat pizza options not visible after applying 'FILTRU_NU_CARNE'"
