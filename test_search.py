import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_search(unittest.TestCase):
    CAUTA_PRODUSE = (By.ID, 'search_key_')
    CLICKSEARCH = (By.ID, 'search_button_')
    REZULTATE = (By.XPATH, "//h1[contains(text(), 'Rezultatele căutării')]")
    PIZZA = (By.XPATH, '/html/body/div[2]/div[3]/div/nav/ul/li[2]/a')
    PROMOTIONALE = (By.CSS_SELECTOR, "button.searchtag.js-searchtag.tag-promo")
    PROMO_MESSAGE = (By.XPATH, '/html/body/div[2]/main/article/div[1]/aside/div[2]')

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self):
        self.chrome.quit()

    def test_search(self):
        self.chrome.find_element(*self.CAUTA_PRODUSE).send_keys('pizza')
        self.chrome.find_element(*self.CLICKSEARCH).click()
        results = self.chrome.find_element(*self.REZULTATE)
        self.assertTrue(results.is_displayed(), "Text 'Rezultatele căutării' is not displayed")

    def test_shopping_cart(self):
        self.chrome.find_element(*self.PIZZA).click()
        self.chrome.find_element(*self.PROMOTIONALE).click()
        promo_element = self.chrome.find_element(*self.PROMO_MESSAGE)
        self.assertIn('Sunt afișate produsele promoționale.', promo_element.text)