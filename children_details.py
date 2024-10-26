from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from new import driver_class
driver = driver_class.driver

class has_children:
    def __init__(self):
        if driver_class.has_children == 1:
            driver.find_element(By.CSS_SELECTOR,'[data-test-id="radio-input-personal-has-children"][value="true"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-0-4"]').send_keys(driver_class.number_of_children_a)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-5-12"]').send_keys(driver_class.number_of_children_b)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-13-18"]').send_keys(driver_class.number_of_children_c)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-+18"]').send_keys(driver_class.number_of_children_d)

        else:
            driver.find_element(By.CSS_SELECTOR,'[data-test-id="radio-input-personal-has-children"][value="false"]').click()

        time.sleep(2)