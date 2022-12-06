import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# This is for maximize web window
driver.maximize_window()
driver.implicitly_wait(1)

# URL of website
url = "https://popageorgianvictor.github.io/MyTestSite/"

# Opening the website
driver.get(url)

# Scroll down in page
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.ID, "iFrames"))
time.sleep(2)

# Example without iFrame

driver.find_element(By.ID, 'btnOutFrame').click()
my_alert = driver.switch_to.alert
my_alert_text = my_alert.text
assert my_alert_text == 'Just Clicked Outside iFrame', "Should've gotten outside message"
my_alert.dismiss() # used to click on the 'Cancel' button of the alert


# Example of iFrame

# using 'WebElement'

# I change the focus into the frame
my_frame = driver.find_element(By.ID, 'myFrame2')# here is WebElement
driver.switch_to.frame(my_frame)
driver.find_element(By.CSS_SELECTOR, '.last > li:nth-child(1) > a:nth-child(1)').click()
time.sleep(2)

# if we want to go back and click on the button outside the iFrame, we have to change the focus again
driver.switch_to.default_content()
driver.find_element(By.ID, 'btnOutFrame').click()
print(driver.switch_to.alert.text)
time.sleep(2)
driver.switch_to.alert.dismiss()

# We can specify the id directly
driver.switch_to.frame('myFrame1')
driver.find_element(By.CSS_SELECTOR, '.ddsmoothmenu > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)').click()
time.sleep(2)
print('I clicked in frame')


