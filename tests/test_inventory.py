import pytest
import logging

from page_data import login_credentials, inventory_test_data
from pages.login import LoginPage
from pages.inventory import InventoryPage


# Configure logger
logger = logging.getLogger(__name__)

@pytest.mark.parametrize("driver", ["chrome", "edge"], indirect=True)
def test_inventory_page(driver):
    login = LoginPage(driver)
    login.login_user(login_credentials.username, login_credentials.password)
    logger.info("Login performed successfully")
    
    inventory = InventoryPage(driver)
    assert inventory.get_product_count() == inventory_test_data.expected_product_count, \
        "Product count does not match expected value."
    logger.info("Product count verified successfully")
    
    assert all(name in inventory.get_product_names() for name in inventory_test_data.product_names), \
        f"One or more products not found in product names."
    logger.info("Product names verified successfully")
        
    inventory.add_to_cart(inventory_test_data.product_names)
    assert inventory.carted_product_number() == len(inventory_test_data.product_names), \
        "Cart count does not match expected value."
    logger.info("Cart count verified successfully")
        