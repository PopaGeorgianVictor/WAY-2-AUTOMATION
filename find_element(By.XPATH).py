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

# The form elements can be located like this:

driver.find_element(By.XPATH, "/html/body/form[1]") # absolute path (would break if the HTML was changed only slightly)
driver.find_element(By.XPATH, "//form[1]") # first form element in the HTML
driver.find_element(By.XPATH, "//form[@id='loginForm']") # the form element with attribute id set to loginForm

# The username element can be located like this:

driver.find_element(By.XPATH, "//form[input/@name='username']") # first form element with an input child element with name set to username
driver.find_element(By.XPATH, "//form[@id='loginForm']/input[1]") # first input child element of the form element with attribute id set to loginForm
driver.find_element(By.XPATH, "//input[@name='username']") # first input element with attribute name set to username

# The “Clear” button element can be located like this:

driver.find_element(By.XPATH, "//input[@name='continue'][@type='button']") # input with attribute name set to continue and attribute type set to button
driver.find_element(By.XPATH, "//form[@id='loginForm']/input[4]") # fourth input child element of the form element with attribute id set to loginForm