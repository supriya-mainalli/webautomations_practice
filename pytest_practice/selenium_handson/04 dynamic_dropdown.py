from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("Ind")

drop_downs = driver.find_elements(By.CLASS_NAME, "ui-menu-item")

for country in drop_downs:
    if country.text == "India":
        print("Found the country")
        break

driver.close()
