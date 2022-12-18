from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/sliders")
driver.maximize_window()
driver.implicitly_wait(2)

slider = driver.find_element(By.ID,"myRange")
size = slider.size
w = size['width']
ActionChains(driver).drag_and_drop_by_offset(slider,w/2,0).perform()
