
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# This is for maximize web window
driver.maximize_window()
wait = WebDriverWait(driver, 5)

# URL of website
url = "https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/present_vs_displayed"

# Opening the website
driver.get(url)

try:
    driver.find_element(By.CSS_SELECTOR, '#bmw').click()
    series_6 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value="6-series"]')))
finally:
    driver.quit()