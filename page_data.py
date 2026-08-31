# pages_data.py
from dataclasses import dataclass

@dataclass
class Page:
    marker: str
    url: str
    
@dataclass
class logindetails:
    username: str
    password: str

@dataclass
class InventoryTestData:
    expected_product_count: int
    product_name: str

# Define your pages here
LoginPage = Page(
    marker="login", 
    url="https://www.saucedemo.com/"
    )
InventoryPage = Page(
    marker="inventory", 
    url="https://www.saucedemo.com/inventory.html"
    )
CartPage = Page(
    marker="cart", 
    url="https://www.saucedemo.com/cart.html"
    )

# Credentials for login
login_credentials = logindetails(
    username="standard_user", 
    password="secret_sauce"
    )

# Inventory test data
inventory_test_data = InventoryTestData(
    expected_product_count=6,
    product_name="Sauce Labs Bolt T-Shirt"
    )