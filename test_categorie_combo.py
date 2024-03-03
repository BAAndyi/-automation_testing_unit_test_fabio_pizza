import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Categorie_combo(unittest.TestCase):
    SELECT_PIZZA = (By.XPATH, "//a[@href='https://www.fabiopizza.ro/Pizza' and text()='Pizza']")
    COMBO = (By.XPATH, "/html/body/div[2]/div[3]/div/nav/ul/li[1]/a")
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_categorie_combo(self):
        self.chrome.find_element(*self.SELECT_PIZZA).click()
        assert "Pizza" in self.chrome.title, "Expected 'Pizza' in page title after selecting pizza category"
    def test_combo(self):
        self.chrome.find_element(*self.COMBO).click()
        assert "Fabio Pizza - rețete originale, ingrediente alese" in self.chrome.title, "Expected 'Fabio Pizza - rețete originale, ingrediente alese' in page title after clicking on combo link"










