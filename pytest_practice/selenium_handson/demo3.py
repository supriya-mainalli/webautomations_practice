import time

from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
dropdown = Select(driver.find_element(By.ID, 'dropdown-class-example'))
dropdown.select_by_value('option2')
time.sleep(5)
checkboxs = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for item in checkboxs:
    if item.get_attribute('value')=="option1":
        item.click()
        assert item.is_selected()
        break

# Radio buttons
radiobuttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
for item in radiobuttons:
    if item.get_attribute('value')=='radio1':
        item.click()
        assert item.is_selected()
        print('Item is selected')
        break

# alerts

driver.find_element(By.ID, 'name').send_keys('Supriya')
driver.find_element(By.ID, 'alertbtn').click()
alert = driver.switch_to.alert
assert 'Supriya' in alert.text, "success"
print('alert is selected')
alert.accept()
# alert.dismiss() for rejecting popups

