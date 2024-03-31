import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Contact(unittest.TestCase):
    MENIU = (By.XPATH, "/html/body/div[2]/aside/div[2]/div[2]/div[2]/a[2]")
    CONTACT = (By.XPATH, '//*[@id="menu_11"]/li[8]/a')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_contact(self):
        self.chrome.find_element(*self.MENIU).click()
        self.chrome.find_element(*self.CONTACT).click()
        assert "Contact" in self.chrome.title, "Expected 'Contact' in page title after clicking on Contact link"
