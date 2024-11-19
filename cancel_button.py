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



class Cancel_button_Personal:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-cancel-personal"]').click()


class Cancel_button_Address:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-cancel-address"]').click()


class Cancel_button_Additional:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-cancel-additional"]').click()

class Accept_Cancel:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-dialog-accept-cancel-form"]').click()

class Decline_Cancel:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-dialog-decline-cancel-form"]').click()









