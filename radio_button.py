
from selenium import webdriver
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
driver.find_element(By.CSS_SELECTOR, "input[value='magic fm']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='radio galaxy']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='europa fm']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='rock fm']").click()

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
