from selenium.webdriver.common.by import By

class login_page:
    def __init__(self, driver):
        self.driver = driver
        self.username = "standard_user"
        self.password = "secret_sauce"
        
    def login_user(self):
        self.driver.find_element(By.ID,"user-name").send_keys(self.username)
        self.driver.find_element(By.ID,"password").send_keys(self.password)
        self.driver.find_element(By.ID,"login-button").click()
    