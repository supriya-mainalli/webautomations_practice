import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

#TD, xpath, CSS, name, LinkText, class name
driver.find_element(By.NAME, 'name').send_keys('supriya')

driver.find_element(By.NAME, 'email').send_keys('abc@gmail.com')

# Static dropdown
# select_by_index()
# select_by_value() if any value attribute present
# select_by_visible_text()
dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown.select_by_index(0)
dropdown.select_by_visible_text('Female')

# CSS selector syntax -> tagname[attribute=value'], #id, .class-name
driver.find_element(By.CSS_SELECTOR, "input[id='exampleInputPassword1']").send_keys('1234')

checkbox = driver.find_element(By.ID, 'exampleCheck1')
checkbox.click()
assert checkbox.is_selected()

# css selector #id
driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()

# if not checkbox.is_selected():
#     print("The checkbox is not selected")
#     assert False
#
# print("The checkbox is selected")

# XPATH syntax - //tagname[@attribute='value']
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# CSS syntax - tagname[attribute='value']
message = driver.find_element(By.CLASS_NAME, 'alert-success').text
assert 'Success' in message

time.sleep(2)

driver.find_element(By.XPATH, "//input[@class='ng-untouched ng-pristine ng-valid']").send_keys("helloagain")
driver.close()
