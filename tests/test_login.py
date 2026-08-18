from selenium import webdriver
from selenium.webdriver.common.by import By
from page_data import InventoryPage


def test_valid_login():

    driver = webdriver.Chrome()
    inventory_page = InventoryPage

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert driver.current_url == inventory_page.url

    driver.quit()