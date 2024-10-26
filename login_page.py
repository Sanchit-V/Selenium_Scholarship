from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from new import driver_class

language = driver_class.language

pass_key=driver_class.pass_key

class login_page():
    def __init__(self):

        if language==1:
            driver_class.driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-en-US-language"]').click()
            time.sleep(3)
            driver_class.driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-login-access-code"]').send_keys(pass_key)
            driver_class.driver.find_element(By.CSS_SELECTOR,'[data-test-id="btn-handle-acess-code-visibility-login"]').click()
            driver_class.driver.find_element(By.CSS_SELECTOR,'[data-test-id="btn-submit-login"]').click()
            time.sleep(2)



        else:
            driver_class.driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-es-ES-language"]').click()
            driver_class.driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-login-access-code"]').send_keys(pass_key)
            driver_class.driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-handle-acess-code-visibility-login"]').click()
            driver_class.driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-submit-login"]').click()
            time.sleep(2)



        