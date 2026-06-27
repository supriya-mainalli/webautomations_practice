from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.switch_to.frame('courses-iframe') # we can pass iframe id or name
iframe_text = driver.find_element(By.XPATH, "//div[@class='container-fluid']//h2//span[1]").text
assert 'An Academy to' in iframe_text
# switch back to original page or default content

driver.switch_to.default_content()
default_text = driver.find_element(By.TAG_NAME, 'h1').text
assert 'Practice Page' == default_text
driver.close()