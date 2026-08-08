from selenium.webdriver.common.by import By

class inventory_page:
    def __init__(self, driver):
        self.driver = driver
        self.total_products_field = (By.CSS_SELECTOR,".inventory_item")
        self.product_name_field = (By.CSS_SELECTOR,".inventory_item_name")
        self.all_product_list = []
        
    def get_product_count(self):
        return len(self.driver.find_elements(*self.total_products_field))
    
    def get_product_names(self):
        product_names = self.driver.find_elements(*self.product_name_field)
        return [name.text for name in product_names]
    
    def all_products_info(self):
        print("="*50)
        for product in self.driver.find_elements(*self.total_products_field):
            each_product = product.text.splitlines()
            self.all_product_list.append(each_product)
            print(product.text)
            print("-"*100)
            
    def product_item_name(self):
        product_names = self.driver.find_elements(By.CSS_SELECTOR,".inventory_item_name")
        return [name.text for name in product_names]
    
    def add_to_cart(self, product_name):
        product = self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        product.click()