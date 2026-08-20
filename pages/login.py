from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class login_page:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        
    def enter_username(self, username):
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.username_field)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.password_field)
        ).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def login_user(self, username, password):
        """Perform full login and return InventoryPage object"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()