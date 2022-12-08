# importing webdriver from selenium

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# create driver object
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))



# URL of website
url = "https://popageorgianvictor.github.io/MyTestSite/"

# Opening the website
driver.get(url)

# Interacting with web element

# Maximize web window

driver.maximize_window()

# Performing click event

click = driver.find_element(By.CSS_SELECTOR, '#loginForm > a:nth-child(8)')
click.click()

# Sending inputs

username = driver.find_element(By.NAME, 'username')
username.send_keys('username')

password = driver.find_element(By.NAME, 'password')
password.send_keys('password')

# Clearing inputs

username = driver.find_element(By.XPATH, '/html/body/form/input[1]')
username.clear()

password = driver.find_element(By.XPATH, '/html/body/form/input[2]')
password.clear()

# Navigating forward/back in browser history

driver.find_element(By.LINK_TEXT, 'Continue').click()
driver.forward()
driver.back()


# Closing browser

driver.close() # close current tab
driver.quit() # close all tabs

# Refresh/reload a web page

driver.refresh()