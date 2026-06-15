from tabnanny import check

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# from demo3 import radiobuttons

driver = webdriver.Chrome()
driver. get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(2)
driver.find_element(By.NAME, 'name').send_keys('Supriya')
driver.find_element(By.NAME, 'email').send_keys('test123@yopmail.com')
driver.find_element(By.XPATH, "//input[@type='password']").send_keys('test1234')
checkbox = driver.find_element(By.ID, 'exampleCheck1')
checkbox.click()
assert checkbox.is_selected() == True, 'Checkbox not selected'

dropdown1 = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown1.select_by_index(0)

dropdown1.select_by_visible_text('Female')

radiobutton = driver.find_element(By.ID, 'inlineRadio2')
radiobutton.click()
assert radiobutton.is_selected() == True, 'Radio button not selected'
driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
time.sleep(2)
driver.refresh()
driver.maximize_window()
driver.close()