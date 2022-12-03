from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# def is_element_present(how, what):
#     if len(driver.find_elements(by=how, value=what)) == 0:
#         return False
#     else:
#         return True

# create driver object
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# This is for maximize web window
driver.maximize_window()
driver.implicitly_wait(5)
# URL of website
url = "https://popageorgianvictor.github.io/MyTestSite/"

# Opening the website
driver.get(url)


# verify number of checkboxes and they are selectable



element = driver.find_element(By.XPATH, "html body form#loginForm div input")
element.click()
# driver.find_element(By.XPATH,'/html/body/form/div[7]/div/input[2]')
# driver.find_element(By.XPATH,'/html/body/form/div[7]/div/input[3]')
# driver.find_element(By.XPATH,'/html/body/form/div[7]/div/input[4]')
# i =1
# while is_element_present(By.XPATH, "//div[7]/input["+str(i)+"]"):
#     driver.find_element(By.XPATH,"//div[7]/input["+str(i)+"]").click()
#     i += 1
#
# print("Total checkboxes are : ",i-1)
# block = driver.find_element(By.XPATH,"/html/body/form/div[7]/div/label")
# checkboxes = block.find_elements(By.NAME,"age-group-checkbox")
#
# print(len(checkboxes))
#
# for checkbox in checkboxes:
#     print("Before clicking : ",checkbox.is_selected())
#     checkbox.click()
#     print("After clicking : ", checkbox.is_selected())
