import pytest
import logging

from page_data import login_credentials, inventory_page
from pages.login import LoginPage

# Configure logger
logger = logging.getLogger(__name__)

@pytest.mark.parametrize("driver", ["chrome", "edge"], indirect=True)
def test_valid_login(driver):
    login = LoginPage(driver)

    logger.info("Starting login test")
    login.login_user(login_credentials.username, login_credentials.password)
    logger.info("Login performed")

    assert driver.current_url == inventory_page.url
    logger.info("URL verified successfully")