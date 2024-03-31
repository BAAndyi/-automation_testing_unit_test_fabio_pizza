import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_scoatem_ingredient(unittest.TestCase):
    SELECT_PIZZA_MENU_BUTTON = (By.XPATH, "//a[@href='https://www.fabiopizza.ro/Pizza' and text()='Pizza']")
    SELECT_PIZZA = (By.XPATH, "//div[contains(@class, 'plist-item-wrapper') and //p[@class='plist_title' and contains(text(), 'Pizza Abruzzo')]]")
    SCOATEM_INGREDIENT_DA = (By.XPATH, '//p[contains(text(),"Vrei să scoți")]//following-sibling::div//button[contains(text(),"Da")]')
    SCOATEM_SALAM_PICANT = (By.XPATH, '/html/body/div[2]/main/section/div/article/form/div/div[2]/div[2]/div[3]/div/ul/li[4]')
    MESAJ_INGREDIENT_SCOS = (By.XPATH, '//p[@class="shop_pi_extra_rezumat js-removable-list"]')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self) -> None:
        self.chrome.quit()


    def Test_scoatem_ingredient(self):
        self.chrome.find_element(*self.SELECT_PIZZA_MENU_BUTTON).click()
        self.chrome.find_element(*self.SELECT_PIZZA).click()
        self.chrome.find_element(*self.SCOATEM_INGREDIENT_DA).click()
        self.chrome.find_element(*self.SCOATEM_SALAM_PICANT).click()
        expected_message="Fără Salam picant"
        actual_message=self.chrome.find_element(*self.MESAJ_INGREDIENT_SCOS).text
        assert expected_message==actual_message





