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

# elements can be located like this:

driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/form[1]/input[1]") # absolute path (would break if the HTML was changed only slightly)
driver.find_element(By.XPATH, "//form[1]") # first form element in the HTML
driver.find_element(By.XPATH, "//[@id='logName']") # the form element with attribute id set to logName


driver.find_element(By.XPATH, "//form[input/@name='name']") # first form element with an input child element with name set to name
driver.find_element(By.XPATH, "//*[@id='logPassword']") # first input child element of the form element with attribute id set to logPassword
