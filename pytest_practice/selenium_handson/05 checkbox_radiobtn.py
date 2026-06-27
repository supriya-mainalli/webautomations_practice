from selenium import webdriver
from selenium.webdriver.common.by import By


# driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

print(driver.find_element(By.XPATH, "//div[@id='radio-btn-example']/fieldset/legend").text)

radio_buttons = driver.find_elements(By.XPATH, "//input[@name='radioButton']")

for radio_button in radio_buttons:
    radio_button.click()
    print(radio_button.is_enabled())


checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxes:
    checkbox.click()
    assert checkbox.is_selected()


checkbox = driver.find_element(By.ID, "checkBoxOption2")
checkbox.click()
assert not checkbox.is_selected()

# Javascript alerts
name = 'Supriya'
driver.find_element(By.NAME, 'enter-name').send_keys(name)
driver.find_element(By.ID,'alertbtn').click()
alert = driver.switch_to.alert
alertText = alert.text
alert.accept() #to accept the alert
assert name in alertText
# message.dismiss()
driver.close()