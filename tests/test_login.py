import pytest

from page_data import InventoryPage
from pages.login import login_page

@pytest.mark.parametrize("driver", ["chrome", "edge"], indirect=True)
def test_valid_login(driver):
    inventory_page = InventoryPage
    login = login_page(driver)
    login.login_user()
    assert driver.current_url == inventory_page.url