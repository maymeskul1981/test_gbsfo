from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
time.sleep(5)
# Ищем поле для ввода текста
inputElement = driver.find_element_by_name("q")
# Напишем текст ответа в найденное поле
inputElement.send_keys("gbsfo")
inputElement.submit()
time.sleep(5)
toolsElement = driver.find_element_by_id("hdtb-tls").click()
time.sleep(5)
allResult = driver.find_element_by_xpath("//*[text()='За всё время']").click()
time.sleep(5)
allResult = driver.find_element_by_xpath("//*[text()=' За час']").click()
time.sleep(30)
driver.close()