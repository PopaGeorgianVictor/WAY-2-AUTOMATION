from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/search_bar")
driver.maximize_window()
driver.implicitly_wait(2)


# search for ...
search_bar = driver.find_element(By.ID, 'myInput')
search_bar.send_keys('lists')

elem = driver.find_element(By.XPATH,"//a[normalize-space()='LISTS']")
actual = elem.text
expected = "LISTS"
assert actual == expected, f'Error: expected: {expected}, actual: {actual} '


# click on  .. after search
elem.click()
