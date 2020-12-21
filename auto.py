from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()

chrome_browser.get('file:///Users/tonyyang/Desktop/search/cs50_web/index.html')

chrome_browser.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)

driver.close()


# btn = chrome_browser.find_element_by_class_name('btn-default')
