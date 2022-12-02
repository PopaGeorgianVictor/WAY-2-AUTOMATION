# importing webdriver from selenium

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Here FireFox  will be used
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))



# URL of website
url = "https://popageorgianvictor.github.io/MyTestSite/"

# Opening the website
driver.get(url)

# Maximize web window
driver.maximize_window()

# set implicit wait time
driver.implicitly_wait(10) # seconds

# get element after 10 seconds
driver.find_element(By.ID, 'the_slow_image')