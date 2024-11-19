from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import time
from logout_username import Logout_username
from new import driver_class
driver=driver_class.driver

class Back_Button_Address:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-back-address"]').click()

class Back_Button_Additional:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-back-additional"]').click()