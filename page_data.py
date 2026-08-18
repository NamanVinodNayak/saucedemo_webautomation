# pages_data.py
from dataclasses import dataclass

@dataclass
class Page:
    marker: str
    url: str

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