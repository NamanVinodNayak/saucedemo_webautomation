from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.total_products_field = (By.CSS_SELECTOR,".inventory_item")
        self.product_name_field = (By.CSS_SELECTOR,".inventory_item_name")
        self.sort_dropdown = (By.CSS_SELECTOR, ".product_sort_container")
        self.all_product_list = []
        
    def get_product_count(self):
        return len(WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(self.total_products_field)
        ))
    
    def get_product_names(self):
        product_names = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(self.product_name_field)
        )
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
    
    def add_to_cart(self, product_names):
        for name in product_names:
            product = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    f"//div[text()='{name}']/ancestor::div[@class='inventory_item']//button"
                ))
            )
            product.click()
        
    def carted_product_number(self):
        badges = self.driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")
        return int(badges[0].text) if badges and badges[0].text else 0

    def sort_by(self, option):
        """Sort inventory using a SauceDemo sort option value."""
        dropdown = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.sort_dropdown)
        )
        Select(dropdown).select_by_value(option)