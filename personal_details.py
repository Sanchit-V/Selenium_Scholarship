from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from new import driver_class
driver = driver_class.driver
class personal_details:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="select-display-personal-document-type"]').click()

        driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-personal-document-type-Other"]').click()
        # driver.find_element(By.CSS_SELECTOR,'[data-test-id="li-personal-document-type-National identity card"]').click()
        # driver.find_element(By.CSS_SELECTOR,'[data-test-id="li-personal-document-type-Passport"]').click()
        # driver.find_element(By.CSS_SELECTOR,'[data-test-id="li-personal-document-type-Foreigner's identity card"]').click()
        # driver.find_element(By.CSS_SELECTOR,'[data-test-id="li-personal-document-type-RUC"]').click()

        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-document-number"]').send_keys('1563636611')
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="select-display-personal-marital-status"]').click()
        # driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-personal-marital-status-Married"]').click()
        # driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-personal-marital-status-Single"]').click()
        # driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-personal-marital-status-Divorced"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-personal-marital-status-Widowed"]').click()
        # driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-personal-marital-status-Separated"]').click()

        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-profession"]').send_keys('Custom Input')







