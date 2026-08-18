import pytest
from config import BASE_URL
from selenium import webdriver

def create_driver(browser: str):
    """Factory function to create a WebDriver instance."""
    browser = browser.lower()
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Edge(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

@pytest.fixture
def driver(request):
    """Fixture that provides a WebDriver based on test parameter."""
    driver = create_driver(request.param)
    driver.get(BASE_URL)   # always open the base site first
    yield driver
    driver.quit()