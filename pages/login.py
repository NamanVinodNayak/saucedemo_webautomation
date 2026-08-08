from selenium.webdriver.common.by import By

class login_page:
    def __init__(self, driver):
        self.driver = driver
        self.username = "standard_user"
        self.password = "secret_sauce"
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        
    def login_user(self):
        self.driver.find_element(*self.username_field).send_keys(self.username)
        self.driver.find_element(*self.password_field).send_keys(self.password)
        self.driver.find_element(*self.login_button).click()
    