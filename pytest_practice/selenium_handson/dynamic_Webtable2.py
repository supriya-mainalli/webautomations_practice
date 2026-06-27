from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://practice.expandtesting.com/dynamic-table")
time.sleep(2)
headers = driver.find_elements(By.XPATH, '//table/thead/tr/th')
# for header in headers:
#     print(header.text)

rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

for item in rows:
    print(item.text)
    arr = item.text.split(" ")
    if arr[0] == "Chrome":
        print(arr)
        result = [x for x in arr if x.endswith('%')]
        result = " ".join(result)
        print(result)
        assert "0.5%" == result
        break


