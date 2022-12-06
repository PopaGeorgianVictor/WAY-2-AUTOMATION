from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(1)

driver.get("https://popageorgianvictor.github.io/My-Test-Site/")


# Right click action

right_click_menu = driver.find_element(By.XPATH, "/html/body/div/nav/ul/li[4]/a")
ActionChains(driver).context_click(right_click_menu).perform()# context click = right click

