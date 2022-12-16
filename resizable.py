from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://jqueryui.com/resources/demos/resizable/default.html")
driver.maximize_window()
driver.implicitly_wait(2)


