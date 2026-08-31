import pytest
import logging

from page_data import InventoryPage, login_credentials, inventory_test_data
from pages.login import login_page
from pages.inventory import inventory_page


# Configure logger
logger = logging.getLogger(__name__)

@pytest.mark.parametrize("driver", ["chrome", "edge"], indirect=True)
def test_inventory_page(driver):
    login = login_page(driver)
    login.login_user(login_credentials.username, login_credentials.password)
    
    inventory = inventory_page(driver)
    assert inventory.get_product_count() == inventory_test_data.expected_product_count, \
        "Product count does not match expected value."
    
    assert all(name in inventory.get_product_names() for name in inventory_test_data.product_names), \
        f"One or more products not found in product names."
        
    inventory.add_to_cart(inventory_test_data.product_names)
    assert inventory.carted_product_number() == len(inventory_test_data.product_names), \
        "Cart count does not match expected value."
        