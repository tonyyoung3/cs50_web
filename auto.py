from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()

chrome_browser.get('file:///Users/tonyyang/Desktop/search/cs50_web/index.html')

chrome_browser.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)

# // Initialize and wait till element(link) became clickable - timeout in 10 seconds
first = WebDriverWait(chrome_browser, 10).until(EC.element_to_be_clickable((By.XPATH,"//a/h3")))

print(first.text)

chrome_browser.close()


# btn = chrome_browser.find_element_by_class_name('btn-default')
