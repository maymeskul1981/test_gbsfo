from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
time.sleep(5)
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("gbsfo")
inputElement.submit()
time.sleep(5)
toolsElement = driver.find_element_by_id("hdtb-tls").click()
time.sleep(5)
allResult = driver.find_element_by_xpath("//*[text()='Все результаты']").click()
time.sleep(5)
allResult = driver.find_element_by_xpath("//*[text()='Точное соответствие']").click()
time.sleep(5)
cur_url = driver.current_url
print(cur_url)
driver.execute_script(f"window.open(\"{cur_url}\", 'new_window')")
time.sleep(30)
driver.close()

