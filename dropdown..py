import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager



driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# This is for maximize web window
driver.maximize_window()

# URL of website
url = "https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/dropdown"

# Opening the website
driver.get(url)



# # using Select class
my_dropdown = driver.find_element('id', 'coding-language-select')
dropdown_object = Select(my_dropdown)
dropdown_object.select_by_value("Python")
dropdown_object.select_by_value('Java')
dropdown_object.select_by_value('PHP')
dropdown_object.select_by_value('C#')
dropdown_object.select_by_value('SQL')

all_options = dropdown_object.options
for option in all_options:
    print(option.text)

# using CSS
dropdown_btn = driver.find_element('id', 'dropdownMenuButton')
dropdown_btn.click()
my_option = driver.find_element('link text', 'PORTOFOLIO')
my_option.click()

driver.find_element(By.LINK_TEXT, 'OVERVIEW').click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
print("Second window title = " + driver.title)

try:
    driver.find_element(By.CSS_SELECTOR,"span[title='PORTOFOLIO']")
    print('Element exist')

except NoSuchElementException:
    print("Element does not exist")