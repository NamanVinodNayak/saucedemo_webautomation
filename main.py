from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import login_page

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(2)
#Page Title
print(f"Page Title: {driver.title}")

login_page = login_page(driver)
login_page.login_user()