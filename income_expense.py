from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from new import driver_class
driver = driver_class.driver

class income_expense:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-monthly-income"]').send_keys('3000000')
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-monthly-expense"]').send_keys('30000')

class financially_independent:
    def __init__(self):
        if financially_independent == 1:
            driver.find_element(By.CSS_SELECTOR,'[data-test-id="radio-input-personal-financially-dependent"][value="true"]').click()

        else:
            driver.find_element(By.CSS_SELECTOR,'[data-test-id="radio-input-personal-financially-dependent"][value="false"]').click()