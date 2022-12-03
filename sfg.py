url = "https://www.uci.org/road/teams"
 
browser = webdriver.Firefox()
browser.get(url)
 
link = browser.find_element_by_link_text('Members')
link.click()
 
menu = browser.find_element_by_css_selector('.export-btn')
menu.click()