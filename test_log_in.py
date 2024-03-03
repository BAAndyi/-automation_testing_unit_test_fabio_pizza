import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_login(unittest.TestCase):
    LOGARE = (By.XPATH, "//a[@class='topbar-but but-account js-login-splash-trigger' and @title='Conectare']")
    MAIL = (By.XPATH, "//input[@id='login_email']")
    SELECT_PAROLA = (By.XPATH, "//input[@id='login_password']")
    CONNECT = (By.XPATH, "//button[@id='login_do']")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self) -> None:
        self.chrome.quit()
    def test_log_in(self):
        self.chrome.find_element(*self.LOGARE).click()
        self.chrome.find_element(*self.MAIL).send_keys("andy.alexandrub@gmail.com")
        self.chrome.find_element(*self.SELECT_PAROLA).send_keys("fab123pizza321")
        self.chrome.find_element(*self.CONNECT).click()
        assert "Conectare" not in self.chrome.title, "The page title should not contain 'Conectare' after successful login"



