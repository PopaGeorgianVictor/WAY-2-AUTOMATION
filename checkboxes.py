import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By



driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# This is for maximize web window
driver.maximize_window()


url = "https://popageorgianvictor.github.io/MyTestSite/"

# Opening the website
driver.get(url)

# scroll down in page
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.ID, "checkboxes"))
time.sleep(3)

# verify number of checkboxes and they are selectable
expected_number_of_options = 4
all_checkboxes = driver.find_elements(By.NAME, 'age-group-checkbox')
assert len(all_checkboxes) == expected_number_of_options, "Number of checkboxes is not the expected"

for checkbox in all_checkboxes:
    checkbox.click()
    value = checkbox.get_attribute('value')
    if checkbox.is_selected():
        print(f"Checkbox with value '{value}' is selectable")
    else:
        raise Exception(f"Value '{value}' is not selectable")



