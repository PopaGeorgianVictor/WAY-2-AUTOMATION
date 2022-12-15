
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By



driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# maximize web window
driver.maximize_window()


# URL of website
url = "https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/iFrame"

# Opening the website
driver.get(url)


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


# if we want to go back and click on the button outside the iFrame, we have to change the focus again
driver.switch_to.default_content()
driver.find_element(By.ID, 'btnOutFrame').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()

# We can specify the id directly
driver.switch_to.frame('myFrame1')
driver.find_element(By.CSS_SELECTOR, '.ddsmoothmenu > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)').click()
print('I clicked in frame')


# to find out how many frame's are on the page
frames = driver.find_elements(By.TAG_NAME,"iFrame")

for frame in frames:
    print(frame.get_attribute("id"))

print(len(frames))

