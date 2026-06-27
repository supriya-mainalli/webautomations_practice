from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "name").send_keys("supriya")


driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert

alert_text = alert.text

if "knowledge" in alert_text:
    print("The alert text is {}".format(alert_text))
    alert.accept()  # accept the alert

driver.find_element(By.ID, "confirmbtn").click()

alert2 = driver.switch_to.alert

alert2_text = alert.text

if "confirm" in alert2_text:
    print("The alert2 text is {}".format(alert2_text))
    alert2.dismiss()
    print("Cancelling the alert box")

driver.close()
