import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By



driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# This is for maximize web window
driver.maximize_window()

# URL of website
url = "https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/all_in_one"

# Opening the website
driver.get(url)


driver.find_element(By.CSS_SELECTOR, '.button').click()
print("Before switching focus: " + driver.title)
all_window_handles = driver.window_handles
original_window_handle = all_window_handles[0]
new_window = all_window_handles[1]
driver.switch_to.window(new_window)
print("After switching focus: " + driver.title)
print("Closing tab")
driver.close()
print("Switching back to original")
driver.switch_to.window(original_window_handle)
