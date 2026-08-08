from selenium.webdriver.common.by import By

class inventory_page:
    def __init__(self, driver):
        self.driver = driver
        self.total_products = driver.find_elements(By.CSS_SELECTOR,".inventory_item")
        
    def get_product_count(self):
        return len(self.total_products)
    
    def print_product_details(self):
        print("-"*50)
        for product in self.total_products:
            print(product.text)
            print("-"*50)