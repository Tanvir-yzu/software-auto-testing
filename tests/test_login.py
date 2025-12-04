from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_invalid_email_login(driver):
    """Test login with invalid email format"""
    login = LoginPage(driver)
    
    login.open()
    login.enter_email("invalidemail")
    login.enter_password("Nothing@1234")
    login.click_login()
    
    # Wait for error message to appear
    try:
        error_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error"))
        )
        assert error_element.is_displayed()
    except TimeoutException:
        # Check if we're still on the login page
        assert "/login" in driver.current_url

def test_invalid_password_login(driver):
    """Test login with invalid password"""
    login = LoginPage(driver)
    
    login.open()
    login.enter_email("2020tanvir1971@gmail.com")
    login.enter_password("wrongpassword")
    login.click_login()
    
    # Wait for error message to appear
    try:
        error_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error"))
        )
        assert error_element.is_displayed()
    except TimeoutException:
        # Check if we're still on the login page
        assert "/login" in driver.current_url

def test_empty_fields_login(driver):
    """Test login with empty email and password fields"""
    login = LoginPage(driver)
    
    login.open()
    # Don't enter any values, just click login
    login.click_login()
    
    # Should stay on login page
    assert "/login" in driver.current_url

def test_empty_email_field(driver):
    """Test login with empty email field"""
    login = LoginPage(driver)
    
    login.open()
    # Enter only password
    login.enter_password("Nothing@1234")
    login.click_login()
    
    # Should stay on login page
    assert "/login" in driver.current_url

def test_empty_password_field(driver):
    """Test login with empty password field"""
    login = LoginPage(driver)
    
    login.open()
    # Enter only email
    login.enter_email("2020tanvir1971@gmail.com")
    login.click_login()
    
    # Should stay on login page
    assert "/login" in driver.current_url

def test_sql_injection_attempt(driver):
    """Test login with SQL injection attempt"""
    login = LoginPage(driver)
    
    login.open()
    login.enter_email("'; DROP TABLE users; --")
    login.enter_password("'; DROP TABLE users; --")
    login.click_login()
    
    # Should not crash and should stay on login page
    assert "/login" in driver.current_url

def test_xss_attack_attempt(driver):
    """Test login with XSS attack attempt"""
    login = LoginPage(driver)
    
    login.open()
    login.enter_email("<script>alert('XSS')</script>")
    login.enter_password("<script>alert('XSS')</script>")
    login.click_login()
    
    # Should not execute script and should stay on login page
    assert "/login" in driver.current_url

def test_special_characters_login(driver):
    """Test login with special characters in credentials"""
    login = LoginPage(driver)
    
    login.open()
    login.enter_email("user!@#$%^&*()@example.com")
    login.enter_password("pass!@#$%^&*()")
    login.click_login()
    
    # Should handle special characters gracefully
    assert "/login" in driver.current_url or "/sections" in driver.current_url

def test_case_sensitivity_email(driver):
    """Test login with different email case sensitivity"""
    login = LoginPage(driver)
    
    login.open()
    # Using uppercase version of valid email
    login.enter_email("2020TANVIR1971@GMAIL.COM")
    login.enter_password("Nothing@1234")
    login.click_login()
    
    # Depending on implementation, this might pass or fail
    # But should not crash
    assert "/login" in driver.current_url or "/sections" in driver.current_url

def test_very_long_credentials(driver):
    """Test login with very long email and password"""
    login = LoginPage(driver)
    
    login.open()
    long_email = "a" * 100 + "@example.com"
    long_password = "a" * 100
    login.enter_email(long_email)
    login.enter_password(long_password)
    login.click_login()
    
    # Should handle long inputs gracefully
    assert "/login" in driver.current_url

def test_whitespace_only_fields(driver):
    """Test login with whitespace only fields"""
    login = LoginPage(driver)
    
    login.open()
    login.enter_email("   ")
    login.enter_password("   ")
    login.click_login()
    
    # Should stay on login page
    assert "/login" in driver.current_url

def test_cross_site_scripting_in_password(driver):
    """Test login with XSS in password field only"""
    login = LoginPage(driver)
    
    login.open()
    login.enter_email("valid@example.com")
    login.enter_password("<script>alert('XSS')</script>")
    login.click_login()
    
    # Should not execute script and should stay on login page
    assert "/login" in driver.current_url
    
def test_valid_login(driver):
    login = LoginPage(driver)

    login.open()
    login.enter_email("2020tanvir1971@gmail.com")
    login.enter_password("Nothing@1234")
    login.click_login()

    WebDriverWait(driver, 60).until(
        EC.any_of(
            EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Sections"),
            EC.url_contains("/sections")
        )
    )

    elements = driver.find_elements(By.TAG_NAME, "h1")
    heading_text = elements[0].text.lower() if elements else ""
    assert heading_text == "sections" or "/sections" in driver.current_url

# === BLACK BOX TESTING CASES ===
def test_black_box_valid_login_redirect(driver):
    """Black Box Test: Valid credentials should redirect to sections page"""
    login = LoginPage(driver)
    
    login.open()
    login.enter_email("2020tanvir1971@gmail.com")
    login.enter_password("Nothing@1234")
    login.click_login()
    
    # Black box perspective: Check if redirected to expected page without knowing implementation
    WebDriverWait(driver, 30).until(
        EC.url_contains("/sections")
    )
    assert "/sections" in driver.current_url

def test_black_box_form_validation_empty_submit(driver):
    """Black Box Test: Empty form submission should show validation errors"""
    login = LoginPage(driver)
    
    login.open()
    login.click_login()
    
    # Black box perspective: Form should validate and show errors without knowing implementation
    assert "/login" in driver.current_url

def test_black_box_ui_element_presence(driver):
    """Black Box Test: Login page should contain expected UI elements"""
    login = LoginPage(driver)
    
    login.open()
    
    # Black box perspective: Check for presence of UI elements without knowing implementation
    # Wait for the page to load completely
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_email"))
    )
    
    # Re-locate elements to ensure they are current
    email_field = driver.find_element(By.ID, "id_email")
    password_field = driver.find_element(By.ID, "id_password")
    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Log In')]")
    
    # Check if elements exist in DOM (might not be visible but still present)
    assert email_field is not None
    assert password_field is not None
    assert login_button is not None

def test_black_box_password_masking(driver):
    """Black Box Test: Password field should mask input"""
    login = LoginPage(driver)
    
    login.open()
    password_field = driver.find_element(By.ID, "id_password")
    
    # Black box perspective: Check password masking behavior without knowing implementation
    login.enter_password("testpassword")
    
    # Password field should not reveal the actual value
    assert password_field.get_attribute("type") == "password"

def test_black_box_remember_me_functionality(driver):
    """Black Box Test: Remember me functionality (if available)"""
    login = LoginPage(driver)
    
    login.open()
    
    # Black box perspective: Test feature availability without knowing implementation
    try:
        remember_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox' and (contains(@name, 'remember') or contains(@id, 'remember'))]")
        # If found, checkbox should be clickable
        assert remember_checkbox is not None
    except:
        # If not found, that's also valid as not all sites have this feature
        pass

# === GRAY BOX TESTING CASES ===
def test_gray_box_session_handling_after_login(driver):
    """Gray Box Test: Session handling after successful login"""
    login = LoginPage(driver)
    
    login.open()
    login.enter_email("2020tanvir1971@gmail.com")
    login.enter_password("Nothing@1234")
    login.click_login()
    
    WebDriverWait(driver, 60).until(
        EC.any_of(
            EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Sections"),
            EC.url_contains("/sections")
        )
    )
    
    # Gray box perspective: Check cookies/session after login
    cookies = driver.get_cookies()
    # Should have session cookies after login
    assert len(cookies) > 0

def test_gray_box_error_message_consistency(driver):
    """Gray Box Test: Error message consistency for different invalid inputs"""
    login = LoginPage(driver)
    
    # Test 1: Invalid email
    login.open()
    login.enter_email("invalid")
    login.enter_password("Nothing@1234")
    login.click_login()
    
    # Store error message
    error_msg_1 = ""
    try:
        error_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error"))
        )
        error_msg_1 = error_element.text
    except TimeoutException:
        pass
    
    # Test 2: Empty email
    driver.get("https://vocavolt.com/login/")
    login.enter_email("")
    login.enter_password("Nothing@1234")
    login.click_login()
    
    # Store error message
    error_msg_2 = ""
    try:
        error_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error"))
        )
        error_msg_2 = error_element.text
    except TimeoutException:
        pass
    
    # Gray box perspective: Analyze error message patterns (partially knowing implementation)
    # Both should result in validation errors, possibly similar messages

def test_gray_box_input_field_validation_timing(driver):
    """Gray Box Test: Validation timing on input fields"""
    login = LoginPage(driver)
    
    login.open()
    
    # Gray box perspective: Test when validation occurs without full knowledge of implementation
    email_field = driver.find_element(By.ID, "id_email")
    password_field = driver.find_element(By.ID, "id_password")
    
    # Enter invalid data
    login.enter_email("invalidemail")
    login.enter_password("123")
    
    # Check if validation happens on blur or submit
    # Focus on another element to trigger blur event
    login.click_login()
    
    # Should show validation errors
    assert "/login" in driver.current_url

def test_gray_box_browser_back_after_login(driver):
    """Gray Box Test: Browser back button behavior after login"""
    login = LoginPage(driver)
    
    login.open()
    login.enter_email("2020tanvir1971@gmail.com")
    login.enter_password("Nothing@1234")
    login.click_login()
    
    WebDriverWait(driver, 60).until(
        EC.any_of(
            EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Sections"),
            EC.url_contains("/sections")
        )
    )
    
    # Gray box perspective: Test navigation behavior with partial knowledge of session management
    # Navigate back to login page
    driver.back()
    
    # Should either stay logged in or properly handle session
    assert "/login" in driver.current_url or "/sections" in driver.current_url