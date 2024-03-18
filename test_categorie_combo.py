import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Categorie_combo(unittest.TestCase):
    COMBO_MENU_ITEM = (By.XPATH, '//a[contains(text(),"Combo")]')
    COMBO_PRODUCT_TITLE = (By.XPATH, '//p[@class="plist_title"]')
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_titlu_produse_combo(self):
        self.chrome.find_element(*self.COMBO_MENU_ITEM).click()
        is_title_correct_for_all_products = True
        product_list = self.chrome.find_elements(*self.COMBO_PRODUCT_TITLE)
        for product in product_list:
            if "combo" not in product.text:
                is_title_correct_for_all_products = False
        assert is_title_correct_for_all_products is True, f"Error: At least one product has the wrong title"
    def test_combo(self):
        self.chrome.find_element(*self.COMBO).click()
        assert "Fabio Pizza - rețete originale, ingrediente alese" in self.chrome.title, "Expected 'Fabio Pizza - rețete originale, ingrediente alese' in page title after clicking on combo link"










