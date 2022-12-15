

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# create driver object
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))



# URL of website
url = "https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/social_login_form"

# Opening the website
driver.get(url)

# Interacting with web element

# Maximize web window
driver.maximize_window()

# Performing click event
driver.find_element(By.CSS_SELECTOR, '.fb.btn').click()

# Sending inputs
driver.find_element(By.NAME, 'username').send_keys('username')
driver.find_element(By.NAME, 'password').send_keys('password')


# Clearing inputs
driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
driver.find_element(By.XPATH, "//input[@placeholder='Username']").clear()


# Navigating forward/back in browser history
driver.find_element(By.CSS_SELECTOR, '.twitter.btn').click()
driver.forward()
driver.back()


# Closing browser
driver.close() # close current tab
driver.quit() # close all tabs

# Refresh/reload a web page
driver.refresh()