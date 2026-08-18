from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login import login_page
from pages.inventory import inventory_page
from pages.cart import cart_page

driver = webdriver.Edge()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(5)
driver.maximize_window()

#Page Title
print(f"Page Title: {driver.title}")

login_page = login_page(driver)
login_page.login_user()

# assert "inventory" in driver.current_url
# print("Login successful")

# inventory_page = inventory_page(driver)
# print(f"Total Products: {inventory_page.get_product_count()}")
# product_names = inventory_page.get_product_names()

# print(product_names)
# for name in product_names:
#     print(name)
    
# inventory_page.add_to_cart("Sauce Labs Backpack")
# # inventory_page.add_to_cart("Sauce Labs Onesie")
# cart_page = cart_page(driver)
# cart_page.go_to_cart()
# cart_page.checkout()
# cart_page.checkout_info("John", "Snow", "123456")
# cart_page.finish_checkout()
# assert cart_page.order_confirmation() == True
# print("Checkout completed successfully")