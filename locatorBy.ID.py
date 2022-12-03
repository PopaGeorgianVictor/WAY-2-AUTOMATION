
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

# The form element can be located like this
login_form = driver.find_element(By.ID, 'loginForm')
print(login_form)
