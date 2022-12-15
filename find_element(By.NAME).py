
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


# create driver object
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# This is for maximize web window
driver.maximize_window()

# URL of website
url = "https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/register"

# Opening the website
driver.get(url)

# elements can be located like this:
driver.find_element(By.NAME, 'fname').send_keys('first name')
driver.find_element(By.NAME, 'lname').send_keys('last name')
