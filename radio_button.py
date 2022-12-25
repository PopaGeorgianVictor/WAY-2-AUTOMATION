
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By



driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# This is for maximize web window
driver.maximize_window()

# URL of website
url = "https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/radio_btn"

# Opening the websitetest
driver.get(url)


# click all button

try:
    driver.find_element(By.CSS_SELECTOR, "input[value='magic fm']").click()
    print("Magic FM button is clickable")
except WebDriverException:
    print("Magic FM button is not clickable")

try:
    driver.find_element(By.CSS_SELECTOR, "input[value='radio galaxy']").click()
    print("Radio Galaxy button is clickable")
except WebDriverException:
    print("Radio Galaxy button is not clickable")

try:
    driver.find_element(By.CSS_SELECTOR, "input[value='europa fm']").click()
    print("Europa FM  button is clickable")
except WebDriverException:
    print("Europa FM  button is not clickable")

try:
    driver.find_element(By.CSS_SELECTOR, "input[value='rock fm']").click()
    print("Rock FM  button is clickable")
except WebDriverException:
    print("Rock FM button is not clickable")


# verify default is selected
expected_default_value = 'rock fm'
locator_by_value = 'input[name="radio-stations"][value="{value}"]'

default_element = driver.find_element(By.CSS_SELECTOR, locator_by_value.format(value=expected_default_value))
assert default_element.is_selected(), f"The default value of {expected_default_value} is not selected."

# verify number of radio button
expected_values = ['magic fm','radio galaxy','europa fm','rock fm']
all_radios = driver.find_elements(By.NAME, 'radio-stations')
assert len(all_radios) == len(expected_values), "the number of radios does not match the expected." \
                                                "Expected: {}, Actual: {}".format(len(expected_values),len(all_radios))
