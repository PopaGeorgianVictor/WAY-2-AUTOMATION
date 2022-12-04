import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By



driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# This is for maximize web window
driver.maximize_window()

# URL of website
url = "https://popageorgianvictor.github.io/MyTestSite/"

# Opening the website
driver.get(url)

# scroll down in page
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, "/html/body/div/div[3]/form/div/div[4]/div[2]/div[2]/h1/strong/u"))
time.sleep(2)


# check for hidden element
my_btn1 = driver.find_element(By.ID, 'btn1')
print(f"First button text: {my_btn1.text}")

my_btn2 = driver.find_element(By.ID, 'btn2')
print(f"Second button text: {my_btn2.text}")

my_btn3 = driver.find_element(By.ID, 'btn3')
print(f"Third button text: {my_btn3.text}")

my_btn4 = driver.find_element(By.ID, 'btn4')
print(f"Fourth button text: {my_btn4.text}")

if my_btn4.is_displayed():
    my_btn4.click()
else:
    raise Exception("Button 4 is not displayed")