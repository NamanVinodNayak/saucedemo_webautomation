from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.go_to_cart_field = (By.XPATH,"//a[@class='shopping_cart_link']")
        self.checkout_field = (By.ID,"checkout")
        self.cart_items = (By.CSS_SELECTOR, ".cart_item")
        self.cart_item_names = (By.CSS_SELECTOR, ".inventory_item_name")
        self.checkout_first_name = (By.ID, "first-name")
        self.checkout_last_name = (By.ID, "last-name")
        self.checkout_postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.checkout_error = (By.CSS_SELECTOR, "[data-test='error']")
        self.confirmation_message = (By.CSS_SELECTOR, ".complete-header")
        
    def go_to_cart(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.go_to_cart_field)
        ).click()
        try:
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(self.cart_items)
            )
        except TimeoutException:
            inventory_url = self.driver.current_url
            if "inventory.html" not in inventory_url:
                raise
            self.driver.get(inventory_url.replace("inventory.html", "cart.html"))
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(self.cart_items)
            )
        
    def checkout(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.checkout_field)
        ).click()
        try:
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(self.checkout_first_name)
            )
        except TimeoutException:
            current_url = self.driver.current_url
            if "cart.html" not in current_url:
                raise
            self.driver.get(current_url.replace("cart.html", "checkout-step-one.html"))
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(self.checkout_first_name)
            )

    def get_product_names(self):
        return [item.text for item in self.driver.find_elements(*self.cart_item_names)]

    def remove_product(self, product_name):
        remove_button = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='cart_item']//button"
        )
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(remove_button)
        ).click()
        try:
            WebDriverWait(self.driver, 2).until(
                lambda driver: not driver.find_elements(
                    By.XPATH,
                    f"//div[text()='{product_name}']/ancestor::div[@class='cart_item']"
                )
            )
        except TimeoutException:
            button = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(remove_button)
            )
            self.driver.execute_script("arguments[0].click();", button)
            WebDriverWait(self.driver, self.timeout).until(
                lambda driver: not driver.find_elements(
                    By.XPATH,
                    f"//div[text()='{product_name}']/ancestor::div[@class='cart_item']"
                )
            )

    def get_item_count(self):
        return len(self.driver.find_elements(*self.cart_item_names))
        
    def checkout_info(self, first_name, last_name, postal_code):
        for locator, value in (
            (self.checkout_first_name, first_name),
            (self.checkout_last_name, last_name),
            (self.checkout_postal_code, postal_code),
        ):
            field = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            field.clear()
            field.send_keys(value)
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()
        if all((first_name, last_name, postal_code)):
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(self.finish_button)
            )
        else:
            try:
                WebDriverWait(self.driver, 2).until(
                    EC.visibility_of_element_located(self.checkout_error)
                )
            except TimeoutException:
                continue_button = WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located(self.continue_button)
                )
                self.driver.execute_script("arguments[0].click();", continue_button)
                WebDriverWait(self.driver, self.timeout).until(
                    EC.visibility_of_element_located(self.checkout_error)
                )

    def get_checkout_error(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.checkout_error)
        ).text
        
    def finish_checkout(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.confirmation_message)
        )
        
    def order_confirmation(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.confirmation_message)
        ).text