

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

# .html link can be located like this:
driver.find_element(By.LINK_TEXT, 'Radio Button').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Check').click()
print('I clicked on button.Two pages should open !!!')