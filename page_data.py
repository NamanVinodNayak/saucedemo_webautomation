# pages_data.py
from dataclasses import dataclass

@dataclass
class Page:
    marker: str
    url: str
    
@dataclass
class LoginDetails:
    username: str
    password: str

@dataclass
class InventoryTestData:
    expected_product_count: int
    product_names: list

# Define your pages here
login_page = Page(
    marker="login", 
    url="https://www.saucedemo.com/"
    )
inventory_page = Page(
    marker="inventory", 
    url="https://www.saucedemo.com/inventory.html"
    )
cart_page = Page(
    marker="cart", 
    url="https://www.saucedemo.com/cart.html"
    )

# Credentials for login
login_credentials = LoginDetails(
    username="standard_user", 
    password="secret_sauce"
    )
invalid_login_credentials = LoginDetails(
    username="invalid_user",
    password="invalid_password"
    )
locked_out_credentials = LoginDetails(
    username="locked_out_user",
    password="secret_sauce"
    )

# Inventory test data
inventory_test_data = InventoryTestData(
    expected_product_count=6,
    product_names=["Sauce Labs Bolt T-Shirt", "Sauce Labs Backpack"],
    )