# Selenium Python - Web Element Handling Cheat Sheet

## 1. Locating Elements

```python
from selenium.webdriver.common.by import By

# Single element
driver.find_element(By.ID, "username")
driver.find_element(By.NAME, "email")
driver.find_element(By.CLASS_NAME, "btn-primary")
driver.find_element(By.TAG_NAME, "input")
driver.find_element(By.LINK_TEXT, "Sign in")
driver.find_element(By.PARTIAL_LINK_TEXT, "Sign")
driver.find_element(By.CSS_SELECTOR, "div.card > a")
driver.find_element(By.XPATH, "//button[@type='submit']")

# Multiple elements (returns list)
driver.find_elements(By.CLASS_NAME, "product-card")
```

---

## 2. Text Box / Input Fields

```python
elem = driver.find_element(By.ID, "username")

elem.send_keys("supriya")          # type text
elem.clear()                       # clear existing text
elem.send_keys("new_text")         # retype

# Get current value
value = elem.get_attribute("value")

# Get visible text (for non-input elements)
text = elem.text
```

---

## 3. Buttons / Links

```python
driver.find_element(By.ID, "submit-btn").click()
driver.find_element(By.LINK_TEXT, "Forgot Password").click()

# Click via JavaScript (if normal click fails due to overlay)
elem = driver.find_element(By.ID, "submit-btn")
driver.execute_script("arguments[0].click();", elem)
```

---

## 4. Checkboxes

```python
checkbox = driver.find_element(By.ID, "terms")

# Check state
checkbox.is_selected()      # returns True/False

# Click only if not already checked
if not checkbox.is_selected():
    checkbox.click()

# Uncheck only if checked
if checkbox.is_selected():
    checkbox.click()
```

---

## 5. Radio Buttons

```python
radio_buttons = driver.find_elements(By.NAME, "gender")

for rb in radio_buttons:
    if rb.get_attribute("value") == "female":
        rb.click()
        break

# Check which is selected
for rb in radio_buttons:
    if rb.is_selected():
        print(rb.get_attribute("value"))
```

---

## 6. Dropdowns (Select Element)

```python
from selenium.webdriver.support.ui import Select

dropdown = Select(driver.find_element(By.ID, "country"))

# Select by visible text
dropdown.select_by_visible_text("India")

# Select by value attribute
dropdown.select_by_value("IN")

# Select by index (0-based)
dropdown.select_by_index(2)

# Get all options
options = dropdown.options
for opt in options:
    print(opt.text)

# Get currently selected option
selected = dropdown.first_selected_option.text

# Multi-select dropdown
dropdown.select_by_visible_text("Option1")
dropdown.select_by_visible_text("Option2")   # adds to selection

# Deselect (multi-select only)
dropdown.deselect_by_visible_text("Option1")
dropdown.deselect_all()
```

---

## 7. Custom Dropdowns (non-`<select>`, e.g., divs/spans with JS)

```python
# Click to open the dropdown
driver.find_element(By.ID, "custom-dropdown").click()

# Click the desired option from the rendered list
options = driver.find_elements(By.CSS_SELECTOR, "ul.dropdown-list li")
for opt in options:
    if opt.text == "Bengaluru":
        opt.click()
        break
```

---

## 8. Alerts / Pop-ups

```python
# Switch to alert
alert = driver.switch_to.alert

alert.accept()                  # click OK
alert.dismiss()                 # click Cancel

# For prompt alerts
alert.send_keys("some text")
alert.accept()

# Get alert text
text = alert.text
```

---

## 9. Frames / iFrames

```python
# Switch by index
driver.switch_to.frame(0)

# Switch by name/id
driver.switch_to.frame("frame_name")

# Switch by WebElement
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

# Switch back to main document
driver.switch_to.default_content()

# Switch to parent frame (one level up)
driver.switch_to.parent_frame()
```

---

## 10. Windows / Tabs

```python
# Get current window handle
main_window = driver.current_window_handle

# Get all window handles
all_windows = driver.window_handles

# Switch to a new window/tab
for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        break

# Close current window and switch back
driver.close()
driver.switch_to.window(main_window)

# Open new tab via JS
driver.execute_script("window.open('https://example.com');")
```

---

## 11. Mouse Actions (ActionChains)

```python
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)

# Hover over element
element = driver.find_element(By.ID, "menu")
actions.move_to_element(element).perform()

# Right-click (context click)
actions.context_click(element).perform()

# Double-click
actions.double_click(element).perform()

# Drag and drop
source = driver.find_element(By.ID, "drag")
target = driver.find_element(By.ID, "drop")
actions.drag_and_drop(source, target).perform()

# Click and hold + move + release
actions.click_and_hold(source).move_by_offset(100, 0).release().perform()

# Chaining multiple actions
actions.move_to_element(menu).click(submenu_item).perform()
```

---

## 12. Keyboard Actions

```python
from selenium.webdriver.common.keys import Keys

elem = driver.find_element(By.ID, "search")

elem.send_keys("selenium")
elem.send_keys(Keys.ENTER)

# Common keys
Keys.TAB
Keys.ESCAPE
Keys.BACKSPACE
Keys.ARROW_DOWN
Keys.ARROW_UP

# Keyboard shortcuts (e.g., Ctrl+A, Ctrl+C)
elem.send_keys(Keys.CONTROL, "a")   # select all
elem.send_keys(Keys.CONTROL, "c")   # copy

# Using ActionChains for key combos
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
```

---

## 13. File Upload

```python
# Direct send_keys works ONLY if input is type="file" (even if hidden)
upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
upload_input.send_keys("/Users/supriya/Downloads/resume.pdf")
```

---

## 14. Scrolling

```python
# Scroll to a specific element
element = driver.find_element(By.ID, "footer")
driver.execute_script("arguments[0].scrollIntoView(true);", element)

# Scroll down by pixels
driver.execute_script("window.scrollBy(0, 500);")

# Scroll to bottom of page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Scroll to top
driver.execute_script("window.scrollTo(0, 0);")
```

---

## 15. Waits

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Implicit wait (set once, applies globally)
driver.implicitly_wait(10)

# Explicit wait - common conditions
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.ID, "username")))
wait.until(EC.visibility_of_element_located((By.ID, "username")))
wait.until(EC.element_to_be_clickable((By.ID, "submit")))
wait.until(EC.invisibility_of_element_located((By.ID, "loader")))
wait.until(EC.text_to_be_present_in_element((By.ID, "status"), "Success"))
wait.until(EC.alert_is_present())
wait.until(EC.url_contains("dashboard"))
wait.until(EC.title_contains("Home"))

# Fluent wait (custom poll frequency + ignored exceptions)
from selenium.common.exceptions import NoSuchElementException

wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
wait.until(EC.presence_of_element_located((By.ID, "dynamic-element")))
```

---

## 16. Getting Element Attributes & Properties

```python
elem = driver.find_element(By.ID, "username")

elem.get_attribute("value")
elem.get_attribute("class")
elem.get_attribute("href")

elem.is_displayed()      # visible on page?
elem.is_enabled()         # enabled (not disabled)?
elem.is_selected()        # checked/selected (checkbox, radio, option)?

elem.tag_name              # e.g., "input"
elem.size                  # {'height': .., 'width': ..}
elem.location              # {'x': .., 'y': ..}

# CSS property value
elem.value_of_css_property("color")
```

---

## 17. Tables

```python
table = driver.find_element(By.ID, "data-table")

# All rows
rows = table.find_elements(By.TAG_NAME, "tr")

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        print(cell.text)

# Specific cell (row 2, column 3) using XPath
cell = driver.find_element(By.XPATH, "//table[@id='data-table']/tbody/tr[2]/td[3]")
```

---

## 18. Shadow DOM

```python
# Get shadow root
host = driver.find_element(By.CSS_SELECTOR, "custom-element")
shadow_root = driver.execute_script("return arguments[0].shadowRoot", host)

# Find element inside shadow DOM
inner_elem = shadow_root.find_element(By.CSS_SELECTOR, "button")
inner_elem.click()
```

---

## 19. JavaScript Executor (general)

```python
# Set value directly via JS (bypasses send_keys, useful for hidden/readonly fields)
driver.execute_script("arguments[0].value = 'test';", elem)

# Get page title via JS
title = driver.execute_script("return document.title;")

# Highlight an element (debugging)
driver.execute_script("arguments[0].style.border='3px solid red'", elem)
```

---

## 20. Common Exceptions to Handle

```python
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    StaleElementReferenceException,
    TimeoutException,
    ElementClickInterceptedException,
)

try:
    driver.find_element(By.ID, "missing").click()
except NoSuchElementException:
    print("Element not found")
except ElementClickInterceptedException:
    print("Element blocked by overlay - try JS click")
```

---

## Quick Reference: Common Locator Strategies (Priority Order)

1. `By.ID` - fastest, most reliable
2. `By.CSS_SELECTOR` - flexible, fast
3. `By.XPATH` - most flexible, slightly slower, use for complex traversal
4. `By.NAME`, `By.CLASS_NAME` - simple cases
5. `By.LINK_TEXT` / `By.PARTIAL_LINK_TEXT` - for `<a>` tags only

**Tip:** Always prefer explicit waits (`WebDriverWait`) over `time.sleep()` for reliability.
