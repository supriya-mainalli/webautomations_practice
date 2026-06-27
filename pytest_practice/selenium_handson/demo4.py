import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME, 'search-keyword').send_keys('ber')
time.sleep(5)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

for item in results:
    time.sleep(1)
    item.find_element(By.XPATH, 'div/button').click()
    time.sleep(2)
time.sleep(5)

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
time.sleep(5)
print('hi supriya')

wait = WebDriverWait(driver, 10)
