import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_scoatem_ingredient(unittest.TestCase):
    SELECTPIZZA = (By.XPATH, "//a[@href='https://www.fabiopizza.ro/Pizza' and text()='Pizza']")
    SELECTPIZZANEW = (By.XPATH, "//div[contains(@class, 'plist-item-wrapper') and .//p[@class='plist_title' and contains(text(), 'Pizza Abruzzo')]]")
    SCOATEMINGREDIENT = (By.XPATH, '//*[@id="frm_atc"]/div/div[2]/div[2]/div[2]/div/ul/li[1]/button')


    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_scoatem_ingredient(self):
        self.chrome.find_element(*self.SELECTPIZZA).click()
        self.chrome.find_element(*self.SELECTPIZZANEW).click()
        self.chrome.find_element(*self.SCOATEMINGREDIENT).click()




