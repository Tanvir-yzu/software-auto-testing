from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import os

class DriverFactory:
    @staticmethod
    def get_driver():
        # Check if browser preference is set in environment variables
        browser = os.environ.get('BROWSER', 'chrome').lower()
        
        if browser == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument("--start-maximized")
            
            # Check if GeckoDriver path is set
            geckodriver_path = os.environ.get('GECKODRIVER_PATH')
            if geckodriver_path and os.path.exists(geckodriver_path):
                driver = webdriver.Firefox(service=FirefoxService(geckodriver_path), options=options)
            else:
                try:
                    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
                except Exception as e:
                    print(f"Could not download Firefox driver: {e}")
                    print("Please ensure you have internet connection or set GECKODRIVER_PATH environment variable")
                    raise
        else:
            # Default to Chrome
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            
            # Check if ChromeDriver path is set in environment variables
            chromedriver_path = os.environ.get('CHROMEDRIVER_PATH')
            
            if chromedriver_path and os.path.exists(chromedriver_path):
                # Use local ChromeDriver
                driver = webdriver.Chrome(service=ChromeService(chromedriver_path), options=options)
            else:
                # Try to use WebDriverManager (will download if needed)
                try:
                    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
                except Exception as e:
                    print(f"Could not download Chrome driver: {e}")
                    print("Please ensure you have internet connection or set CHROMEDRIVER_PATH environment variable")
                    raise
        
        driver.implicitly_wait(5)
        return driver