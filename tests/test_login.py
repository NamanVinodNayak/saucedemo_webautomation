import pytest
import logging

from page_data import InventoryPage, login_credentials
from pages.login import login_page

# Configure logger
logger = logging.getLogger(__name__)

@pytest.mark.parametrize("driver", ["chrome", "edge"], indirect=True)
def test_valid_login(driver):
    inventory_page = InventoryPage
    login = login_page(driver)

    logger.info("Starting login test")
    login.login_user(login_credentials.username, login_credentials.password)
    logger.info("Login performed")

    assert driver.current_url == inventory_page.url
    logger.info("URL verified successfully")