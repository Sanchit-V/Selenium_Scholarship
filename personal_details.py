from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
from new import driver_class
driver = driver_class.driver
class personal_details:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="select-display-personal-document-type"]').click()

        # driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-personal-document-type-Other"]').click()
        driver.find_element(By.CSS_SELECTOR,'[data-test-id="li-personal-document-type-National identity card"]').click()
        # driver.find_element(By.CSS_SELECTOR,'[data-test-id="li-personal-document-type-Passport"]').click()
        # driver.find_element(By.CSS_SELECTOR,'[data-test-id="li-personal-document-type-Foreigner's identity card"]').click()
        # driver.find_element(By.CSS_SELECTOR,'[data-test-id="li-personal-document-type-RUC"]').click()


        personal_document_box=driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-document-number"]')
        personal_document_box.click()
        personal_document_box.send_keys(Keys.CONTROL+"a")
        personal_document_box.send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-document-number"]').send_keys('21212690')


        driver.find_element(By.CSS_SELECTOR, '[data-test-id="select-display-personal-marital-status"]').click()
        # driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-personal-marital-status-Married"]').click()
        # driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-personal-marital-status-Single"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-personal-marital-status-Divorced"]').click()
        # driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-personal-marital-status-Widowed"]').click()
        # driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-personal-marital-status-Separated"]').click()




        profession_box_input=driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-profession"]')
        profession_box_input.click()
        profession_box_input.send_keys(Keys.CONTROL + "a")
        profession_box_input.send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-profession"]').send_keys('Custom Input')







