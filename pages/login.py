from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")
        
    def enter_username(self, username):
        field = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.username_field)
        )
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.password_field)
        )
        field.clear()
        field.send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def login_user(self, username, password):
        """Perform a full login attempt."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """Return the visible login error message."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.error_message)
        ).text