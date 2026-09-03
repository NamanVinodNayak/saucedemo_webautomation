import pytest
from selenium.webdriver.common.by import By

from pages.login import LoginPage
from pages.inventory import InventoryPage
from pages.cart import CartPage
from page_data import login_credentials as login_page_data
from page_data import inventory_test_data as inventory_page_data


@pytest.mark.parametrize(
    "driver",
    ["chrome", "edge"],
    indirect=True
)
def test_add_product_to_cart(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.login_user(
        login_page_data.username,
        login_page_data.password
    )

    # Add a valid product to the cart
    product_name = inventory_page_data.product_names[0]
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart([product_name])

    # Open cart and verify the selected product is there
    cart_page = CartPage(driver)
    cart_page.go_to_cart()

    assert driver.current_url.endswith("/cart.html")
    assert product_name in driver.page_source
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"

    # Verify checkout button is available
    assert driver.find_element(By.ID, "checkout").is_displayed()
    cart_page.checkout()