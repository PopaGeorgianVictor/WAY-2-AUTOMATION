import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By



driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# This is for maximize web window
driver.maximize_window()

# URL of website
url = "https://popageorgianvictor.github.io/MyTestSite/"

# Opening the website
driver.get(url)

# scroll down in page
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.ID, "windows"))
time.sleep(2)

driver.find_element('xpath', '//*[@id="windows"]/a[1]').click()
print("Before switching focus: " + driver.title)
all_window_handles = driver.window_handles
original_window_handle = all_window_handles[0]
new_window = all_window_handles[1]
driver.switch_to.window(new_window)
print("After switching focus: " + driver.title)
print("Closing tab")
time.sleep(5)
driver.close()
print("Switching back to original")
driver.switch_to.window(original_window_handle)
