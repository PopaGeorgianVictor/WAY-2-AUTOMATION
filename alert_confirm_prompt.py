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

# # html alert
# driver.find_element(By.CSS_SELECTOR, "div#bootStrapAlertExample button").click()
# html_alert_text = driver.find_element(By.ID, "bootStrapAlert").text
# expected_text = "This is alert using just html."
# assert html_alert_text == expected_text, f"Error: expected: {expected_text}, actual: {html_alert_text}"
#
# # js alert accept
# driver.find_element(By.CSS_SELECTOR, "div#jsAlertExample button").click()
# js_alert = driver.switch_to.alert
# js_alert.accept()

# # js confirm accept alert
# driver.find_element(By.CSS_SELECTOR, "div#jsConfirmExample button").click()
# js_confirm = driver.switch_to.alert
# js_confirm.accept()
# rs_message = driver.find_element(By.ID, 'userResponse1').text
# assert rs_message == 'Great! You will love it!', "Wrong message after accepting"

# js confirm cancel alert
driver.find_element(By.CSS_SELECTOR, "div#jsConfirmExample button").click()
js_confirm = driver.switch_to.alert
js_confirm.dismiss()
rs_message = driver.find_element(By.ID, 'userResponse1').text
assert rs_message == "Too bad!!! You would've loved it!", "Wrong message after accepting"