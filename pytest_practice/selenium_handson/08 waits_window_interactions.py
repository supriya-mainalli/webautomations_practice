from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# implicit wait
driver.implicitly_wait(2)
driver.find_element(By.ID, "name").send_keys("supriya")

# explicit wait
wait = WebDriverWait(driver, 2)
wait.until(EC.presence_of_element_located((By.ID, "name")))

# child windows
child_window = driver.window_handles[1]
parent_window = driver.window_handles[0]
driver.find_element(By.ID, "opentab").click()
driver.switch_to.window(child_window)
print("Switched to child window", driver.title)
print("Now switching back to parent window")
driver.switch_to.window(parent_window)
print("Switched to parent window", driver.title)

driver.close()
