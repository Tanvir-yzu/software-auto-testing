from selenium.webdriver.common.by import By

class LoginPage:

    EMAIL = (By.ID, "id_email")
    PASSWORD = (By.ID, "id_password")
    LOGIN_BTN = (By.XPATH, "//button[contains(text(),'Log In')]")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://vocavolt.com/login/")

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()
