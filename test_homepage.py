import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_homepage(unittest.TestCase):
    SELECT_PIZZA_LINK = (By.XPATH, "//a[@href='https://www.fabiopizza.ro/Pizza' and text()='Pizza']")
    SELECT_SPECIFIC_PIZZA = (By.XPATH, "//div[contains(@class, 'plist-item-wrapper') and .//p[@class='plist_title' and contains(text(), 'Pizza Abruzzo')]]")
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

    def test_accesam_pizza(self):
        self.chrome.find_element(*self.SELECT_PIZZA_LINK).click()
        self.chrome.find_element(*self.SELECT_SPECIFIC_PIZZA).click()
        assert "Pizza Abruzzo" in self.chrome.title, "Expected 'Pizza Abruzzo' in page title after selecting specific pizza"

    def test_homepage(self):
        self.chrome.find_element(*self.DESERT).click()
        self.chrome.find_element(*self.HOMEPAGE).click()
        assert "Fabio Pizza" in self.chrome.title, "Expected 'Fabio Pizza' in page title after clicking on homepage link"

    def test_info_utile(self):
        self.chrome.find_element(*self.MENIU).click()
        self.chrome.find_element(*self.INFO_UTILE).click()
        assert "Informații utile" in self.chrome.title, "Expected 'Informații utile' in page title after clicking on info utile link"