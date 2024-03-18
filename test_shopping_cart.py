import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_login_fabiopizza(unittest.TestCase):
    MY_ACCOUNT = (By.XPATH,
                  )
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def setUp(self) -> None:
            self.chrome = webdriver.Chrome()
            self.chrome.maximize_window()
            self.chrome.implicitly_wait(2)
            self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self) -> None:
            self.chrome.quit()

         def test_login_fabiopizza(self):

