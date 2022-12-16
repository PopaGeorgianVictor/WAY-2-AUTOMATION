import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# This is for maximize web window
driver.maximize_window()
driver.implicitly_wait(1)

# URL of website
url = "https://popageorgianvictor.github.io/PRESENTATION-SITE/"

# Opening the website
driver.get(url)


# mouse over
menu = driver.find_element(By.CSS_SELECTOR,"#container a")
action = ActionChains(driver)
action.move_to_element(menu).perform()
print('Mouse over success')

# mouse over and click
print('Click on Portofolio')
driver.find_element(By.XPATH, "//a[contains(text(),'Portofolio')]").click()

