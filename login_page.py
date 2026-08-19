from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from base import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    LOGGED_USER_TEXT = (By.XPATH, "//li/a[contains(text(), 'Logged in as')]")
    ERROR_MSG = (By.XPATH, "//p[contains(text(), 'incorrect')]")
    
    def open(self):
        try:
            self.open_url("https://automationexercise.com/login")
        except Exception:
            pass  # Ignore timeout if page DOM is ready
        self.dismiss_consent_popup()
    
    def dismiss_consent_popup(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        consent_locator = (By.XPATH, "//button[contains(@class, 'fc-button') or contains(text(), 'Consent') or contains(text(), 'Accept')]")
        try:
            short_wait = WebDriverWait(self.driver, 3)
            consent_button = short_wait.until(EC.element_to_be_clickable(consent_locator))
            consent_button.click()
        except TimeoutException:
            pass
    
    def login(self, email, password):
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def is_logged_in(self):
        return self.get_text(self.LOGGED_USER_TEXT)
    
    def get_error_message(self):
        element = self.find(self.ERROR_MSG)
        return element.text
