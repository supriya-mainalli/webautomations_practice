from selenium import webdriver
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')
dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
#dropdwon.select_by_value(1)
dropdown.select_by_index(1)
time.sleep(2)
dropdown.select_by_visible_text('Female')
time.sleep(2)
driver.close()
