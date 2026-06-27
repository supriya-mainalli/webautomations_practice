from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')
time.sleep(5)
print(f" the current url is {driver.current_url}")
print(f"the title is {driver.title}")
driver.find_element(By.NAME, 'name').send_keys('Supriya')
driver.find_element(By.NAME, 'email').send_keys('test123@gmail.com')
driver.find_element(By.CSS_SELECTOR, '#exampleInputPassword1').send_keys('12345')
driver.find_element(By.ID, 'exampleCheck1').click()
driver.find_element(By.XPATH, "//input[@id='inlineRadio1']").click()
driver.find_element(By.XPATH, "//input[@class='ng-untouched ng-pristine ng-valid']").send_keys('supriya')
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(5)
message = driver.find_element(By.CLASS_NAME, "alert-success").text.lower()
assert 'success' in message
driver.close()