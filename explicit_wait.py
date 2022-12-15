
# import necessary classes
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# create driver object
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# URL of website
url = "https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/image_load_slow"

# Opening the website
driver.get(url)

# Maximize web window
driver.maximize_window()


try:
    # wait 10 second before looking for element
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'the_slow_image'))
    )

finally:
    # else quit
    driver.quit()

