from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open_url(self, url):
        max_retries = 3
        for attempt in range(max_retries):
            try:
                self.driver.get(url)
                return
            except WebDriverException as e:
                if "timeout" in str(e).lower() and attempt < max_retries - 1:
                    time.sleep(2)
                    continue
                raise
    
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click(self, locator):
        max_retries = 3
        for attempt in range(max_retries):
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except WebDriverException as e:
                if "timeout" in str(e).lower() and attempt < max_retries - 1:
                    time.sleep(2)
                    continue
                raise
    
    def type_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        element = self.find(locator)
        return element.text
