from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/right_click_menu")


# Right click action

right_click_menu = driver.find_element(By.CSS_SELECTOR, "div#container a")
ActionChains(driver).context_click(right_click_menu).perform()# context click = right click

