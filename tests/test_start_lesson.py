from pages.login_page import LoginPage
from pages.sections_page import SectionsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_start_lesson(driver):
    login = LoginPage(driver)
    sections = SectionsPage(driver)

    login.open()
    login.enter_email("2020tanvir1971@gmail.com")
    login.enter_password("Nothing@1234")
    login.click_login()

    sections.open()
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/wordpack/') and contains(@href,'/flashcard/') and contains(normalize-space(.),'Start')]")
    ))

    sections.click_start_lesson()

    WebDriverWait(driver, 60).until(
        EC.any_of(
            EC.url_contains("/wordpack/"),
            EC.url_contains("/flashcard/")
        )
    )

    assert "/wordpack/" in driver.current_url.lower() and "/flashcard/" in driver.current_url.lower()
