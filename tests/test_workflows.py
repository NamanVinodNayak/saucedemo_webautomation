import pytest

from page_data import (
    invalid_login_credentials,
    inventory_test_data,
    locked_out_credentials,
    login_credentials,
)
from pages.cart import CartPage
from pages.inventory import InventoryPage
from pages.login import LoginPage


@pytest.mark.parametrize("driver", ["chrome", "edge"], indirect=True)
def test_invalid_login_shows_error(driver):
    login_page = LoginPage(driver)

    login_page.login_user(
        invalid_login_credentials.username,
        invalid_login_credentials.password,
    )

    assert "Username and password do not match" in login_page.get_error_message()
    assert "/inventory.html" not in driver.current_url


@pytest.mark.parametrize("driver", ["chrome", "edge"], indirect=True)
def test_locked_out_user_cannot_login(driver):
    login_page = LoginPage(driver)

    login_page.login_user(
        locked_out_credentials.username,
        locked_out_credentials.password,
    )

    assert "locked out" in login_page.get_error_message().lower()
    assert "/inventory.html" not in driver.current_url


@pytest.mark.parametrize("driver", ["chrome", "edge"], indirect=True)
def test_empty_checkout_fields_show_validation_error(driver):
    LoginPage(driver).login_user(
        login_credentials.username,
        login_credentials.password,
    )
    InventoryPage(driver).add_to_cart([inventory_test_data.product_names[0]])

    cart_page = CartPage(driver)
    cart_page.go_to_cart()
    cart_page.checkout()
    cart_page.checkout_info("", "", "")

    assert "First Name is required" in cart_page.get_checkout_error()


@pytest.mark.parametrize("driver", ["chrome", "edge"], indirect=True)
def test_remove_item_from_cart(driver):
    LoginPage(driver).login_user(
        login_credentials.username,
        login_credentials.password,
    )
    inventory_page = InventoryPage(driver)
    products = inventory_test_data.product_names
    inventory_page.add_to_cart(products)

    cart_page = CartPage(driver)
    cart_page.go_to_cart()
    cart_page.remove_product(products[0])

    assert products[0] not in cart_page.get_product_names()
    assert cart_page.get_item_count() == len(products) - 1


@pytest.mark.parametrize("driver", ["chrome", "edge"], indirect=True)
def test_complete_checkout_shows_confirmation(driver):
    LoginPage(driver).login_user(
        login_credentials.username,
        login_credentials.password,
    )
    InventoryPage(driver).add_to_cart([inventory_test_data.product_names[0]])

    cart_page = CartPage(driver)
    cart_page.go_to_cart()
    cart_page.checkout()
    cart_page.checkout_info("Test", "Customer", "12345")
    cart_page.finish_checkout()

    assert cart_page.order_confirmation() == "Thank you for your order!"


@pytest.mark.parametrize("driver", ["chrome", "edge"], indirect=True)
def test_sort_products_a_to_z(driver):
    LoginPage(driver).login_user(
        login_credentials.username,
        login_credentials.password,
    )
    inventory_page = InventoryPage(driver)

    inventory_page.sort_by("az")

    product_names = inventory_page.get_product_names()
    assert product_names == sorted(product_names)