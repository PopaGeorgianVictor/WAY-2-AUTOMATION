
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
url = "https://popageorgianvictor.github.io/MyTestSite/"

# Opening the website
driver.get(url)

# The continue.html link can be located like this:
continue_link = driver.find_element(By.LINK_TEXT, 'Continue')
continue_link_partial = driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')
print(continue_link)
print(continue_link_partial)