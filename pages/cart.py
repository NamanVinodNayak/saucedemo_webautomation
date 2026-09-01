from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.go_to_cart_field = (By.XPATH,"//a[@class='shopping_cart_link']")
        self.checkout_field = (By.ID,"checkout")
        
    def go_to_cart(self):
        self.driver.find_element(*self.go_to_cart_field).click() 
        
    def checkout(self):
        self.driver.find_element(*self.checkout_field).click()
        
    def checkout_info(self, first_name, last_name, postal_code):
        if "checkout-step-one" not in self.driver.current_url:
            raise Exception("Not on the checkout information page")
        self.driver.find_element(By.ID,"first-name").send_keys(first_name)
        self.driver.find_element(By.ID,"last-name").send_keys(last_name)
        self.driver.find_element(By.ID,"postal-code").send_keys(postal_code)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.CSS_SELECTOR,"#continue").click()
        
    def finish_checkout(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH,"//button[@id='finish']").click()
        
    def order_confirmation(self):
        return self.driver.find_element(By.XPATH,"//h2[text()='Thank you for your order!']").is_displayed()