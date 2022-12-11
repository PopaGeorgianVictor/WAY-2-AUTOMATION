import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/alert_confirm_prompt")
driver.maximize_window()
driver.implicitly_wait(2)

# html alert

driver.find_element(By.CSS_SELECTOR, "div#bootStrapAlertExample button").click()
html_alert_text = driver.find_element(By.ID, "bootStrapAlert").text
expected_text = "This is alert using just html."
assert html_alert_text == expected_text, f"Error: expected: {expected_text}, actual: {html_alert_text}"

