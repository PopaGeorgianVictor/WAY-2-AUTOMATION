# importing webdriver from selenium

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# create driver object
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# This is for maximize web window
driver.maximize_window()

# URL of website
url = "https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/all_in_one"

# Opening the website
driver.get(url)

# is more than one element with class name 'button'
# if we do not specify the index, by default it will be 0 (the first element found)
driver.find_elements(By.CLASS_NAME, 'button')[1].click()
print("I clicked on button with index 1")

