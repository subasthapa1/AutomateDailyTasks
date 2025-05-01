from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

import sys
sys.path.append('../')

# Initialize WebDriver
driver = webdriver.Firefox()

# Open Salesforce login page
driver.get('https://login.salesforce.com/')
try:
    # Wait for the username field to be visible
    element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
except Exception as e:
    print(f"Exception occurred: {e}")
    driver.quit()

# Enter username and password
elem = driver.find_element(By.NAME, "username")
elem.clear()
elem.send_keys("s.thapa19@wlv.ac.uk")

elem = driver.find_element(By.NAME, "pw")
elem.clear()
elem.send_keys("ambarkaar@3")

elem = driver.find_element(By.NAME, "Login")
elem.click()

try:
    # Wait for the Salesforce header to be visible
    element = WebDriverWait(driver, 120).until(
        EC.visibility_of_element_located((By.ID, "oneHeader"))
    )
except Exception as e:
    print(f"Exception occurred: {e}")
    driver.quit()

# Get the current HTML content after logging in
html_content = driver.page_source

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
tags = soup.find_all('div')

print(html_content)
print(len(tags))

elem= driver.find_element(By.XPATH, '//div[@class="navexSetupNav"]//button[@title="App Launcher"]')
elem.click()

try:
    # Wait for the Salesforce header to be visible
    element = WebDriverWait(driver, 120).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@part="input-container"]//input[@class="slds-input"]'))
    )
except Exception as e:
    print(f"Exception occurred: {e}")
    driver.quit()

elem = driver.find_element(By.XPATH, '//div[@part="input-container"]//input[@class="slds-input"]')
elem.clear()
elem.send_keys("Sales")
elem = driver.find_element(By.XPATH, '//a[contains(@class, "al-menu-item")]//span/p[./text()="Sales"]')
elem.click()
# Close the WebDriver session
#driver.close()
