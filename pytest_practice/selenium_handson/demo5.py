# Scenario:
# Open google.com
# Wait until search box is VISIBLE
# Type "EPAM QA interview" and search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

