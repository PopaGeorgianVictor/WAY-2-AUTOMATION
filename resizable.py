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
resizable = driver.find_element(By.XPATH, '//*[@id="resizable"]/div[3]')
ActionChains(driver).drag_and_drop_by_offset(resizable,500,500).perform()

# back to original
ActionChains(driver).drag_and_drop_by_offset(resizable,-500,-500).perform()


