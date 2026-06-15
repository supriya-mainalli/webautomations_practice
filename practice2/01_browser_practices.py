from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
print(f"The title of the page is {driver.title}")
print(f"the current url is {driver.current_url}")
driver.find_element(By.NAME, "name").send_keys("supriya")
driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("tests")
checkbox = driver.find_element(By.ID, "exampleCheck1")
checkbox.click()
assert checkbox.is_selected(), "It is not selected"
radiobutton = driver.find_element(By.CSS_SELECTOR, "#inlineRadio2")
radiobutton.click()
assert radiobutton.is_enabled(), "It is not enabled"
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# dropdown.select_by_value("Male")
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)


# dynamic dropdown

driver.quit()