from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/resizable")
driver.maximize_window()
driver.implicitly_wait(2)


# pull the edge for gifts !!!

elem = driver.find_element(By.ID, 'resizable')
print("Original size is", elem.size)
resizable = driver.find_element(By.XPATH, '//*[@id="resizable"]/div[3]')
ActionChains(driver).drag_and_drop_by_offset(resizable,500,500).perform()
print("After resize is", elem.size)

expected_size = {'height': 619, 'width': 619}
actual_size = elem.size
assert expected_size == actual_size, f"Error: expected: {expected_size}, actual: {actual_size}"

# back to original

ActionChains(driver).drag_and_drop_by_offset(resizable,-500,-500).perform()
expected_size = {'height': 119, 'width': 119}
actual_size = elem.size
assert expected_size == actual_size, f"Error: expected: {expected_size}, actual: {actual_size}"

