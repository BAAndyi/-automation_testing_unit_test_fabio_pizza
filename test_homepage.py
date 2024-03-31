import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_homepage(unittest.TestCase):
    NUMBER_OF_MENIU_ITEM = (By.XPATH, '//ul[@class="menu-item mainmenu"]//li')
    DESERT = (By.XPATH, '/html/body/div[2]/div[3]/div/nav/ul/li[5]/a')
    HOMEPAGE = (By.XPATH, '/html/body/div[2]/aside/a/img')
    MENIU = (By.XPATH, "/html/body/div[2]/aside/div[2]/div[2]/div[2]/a[2]")
    INFO_UTILE = (By.XPATH, '//*[@id="menu_11"]/li[5]/a')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self) -> None:
        try:
            self.chrome.quit()
        except Exception as e:
            print(f"Error occurred during teardown: {e}")

    def test_check_meniu_item(self):
        number_of_meniu_items = self.chrome.find_elements(*self.NUMBER_OF_MENIU_ITEM)
        assert len(number_of_meniu_items)==7