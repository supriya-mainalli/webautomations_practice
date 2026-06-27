from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(5)
driver.find_element(By.LINK_TEXT, 'Forgot Password?').click()
# driver.find_element(By.XPATH, "//form/div[1]/input[@id='email']").send_keys('test12')
driver.find_element(By.XPATH, "//button[text()='Request reset link']").click()
driver.close()