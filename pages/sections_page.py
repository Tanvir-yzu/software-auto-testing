from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SectionsPage:
    START_LINK = (By.XPATH, "//a[contains(@href,'/wordpack/') and contains(@href,'/flashcard/') and contains(normalize-space(.),'Start')]")
    START_BUTTON = (By.XPATH, "//a[contains(normalize-space(.),'Start')]")
    START_BUTTON_ALT = (By.XPATH, "//button[contains(normalize-space(.),'Start')]")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://vocavolt.com/sections/")

    def click_start_lesson(self):
        wait = WebDriverWait(self.driver, 30)
        el = None
        for locator in [self.START_LINK, self.START_BUTTON, self.START_BUTTON_ALT]:
            try:
                el = wait.until(EC.element_to_be_clickable(locator))
                break
            except Exception:
                continue
        if el is None:
            raise Exception("Start control not found")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        try:
            el.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", el)
