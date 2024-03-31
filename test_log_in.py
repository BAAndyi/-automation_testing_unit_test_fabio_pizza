import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test_log_in(unittest.TestCase):
    LOGARE = (By.XPATH, "//a[@class='topbar-but but-account js-login-splash-trigger' and @title='Conectare']")
    MAIL = (By.XPATH, "//input[@id='login_email']")
    SELECT_PAROLA = (By.XPATH, "//input[@id='login_password']")
    CONNECT = (By.XPATH, "//button[@id='login_do']")
    ERROR_MESSAGE_PASS = (By.XPATH, "/html/body/article[1]/div/section/form/div[2]")
    ERROR_MESSAGE_MAIL = (By.XPATH, "/html/body/article[1]/div/section/form/div[2]")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://www.fabiopizza.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_log_in_valid_credentials(self):
        self.chrome.find_element(*self.LOGARE).click()
        self.chrome.find_element(*self.MAIL).send_keys("andy.alexandrub@gmail.com")
        self.chrome.find_element(*self.SELECT_PAROLA).send_keys("fab123pizza321")
        self.chrome.find_element(*self.CONNECT).click()

        assert "Conectare" not in self.chrome.title, "The page title will contain, 'Salut,Alexandru' after successful login"

    def test_log_in_invalid_pass(self):
        self.chrome.find_element(*self.LOGARE).click()
        self.chrome.find_element(*self.MAIL).send_keys("andy.alexandrub@gmail.com")
        self.chrome.find_element(*self.SELECT_PAROLA).send_keys("fabwrongbaf")
        self.chrome.find_element(*self.CONNECT).click()
        error_message = ""
        try:

            error_message = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(self.ERROR_MESSAGE_PASS))
            error_message = (self.chrome.find_element(*self.ERROR_MESSAGE_PASS)).text
        except:
            pass
        expected_text = "Parola este greșită."
        assert expected_text in error_message, f"expected error message: {expected_text} actual error message {error_message}"

    def test_log_in_invalid_mail(self):
        self.chrome.find_element(*self.LOGARE).click()
        self.chrome.find_element(*self.MAIL).send_keys("andy.alex@gmail.com")
        self.chrome.find_element(*self.SELECT_PAROLA).send_keys("fab123pizza321")
        self.chrome.find_element(*self.CONNECT).click()
        error_message = ""
        try:

             error_message = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(self.ERROR_MESSAGE_MAIL))
             error_message = (self.chrome.find_element(*self.ERROR_MESSAGE_MAIL)).text
        except:
            pass
        expected_text = "Acest cont nu există!"
        assert expected_text in error_message, f"expected error message: {expected_text} actual error message {error_message}"

