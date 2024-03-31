import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_search(unittest.TestCase):
    CAUTA_PRODUSE = (By.XPATH, '//*[@id="search_form_input"]')
    CLICK_SEARCH = (By.XPATH, '//*[@id="search_button"]')
    REZULTATE = (By.XPATH, '//*[@id="result"]')
    CART = (By.XPATH, "/html/body/div[2]/div[3]/div/div/a/div/svg")
    REDUCERE = (By.XPATH, "/html/body/div[2]/main/article/div[1]/aside/div[1]/div/button[1]/svg")
    PROMO_MESSAGE = (By.XPATH, "/html/body/div[2]/main/article/div[1]/aside/div[2]")

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self):
        self.chrome.quit()

    def test_search(self):
        self.chrome.find_element(*self.CAUTA_PRODUSE).send_keys('pizza')
        self.chrome.find_element(*self.CLICK_SEARCH).click()
        results = self.chrome.find_element(*self.REZULTATE)
        self.assertTrue('Sunt afișate produsele promoționale.' in results.text)

    def test_shopping_cart(self):
        self.chrome.find_element(*self.CART).click()
        self.chrome.find_element(*self.REDUCERE).click()
        promo_element = self.chrome.find_element(*self.PROMO_MESSAGE)
        self.assertIn("Sunt afișate produsele promoționale.", promo_element.text)