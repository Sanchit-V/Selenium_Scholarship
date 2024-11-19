from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import time
from new import driver_class
driver=driver_class.driver



class Logout_username:
    def __init__(self):
        user_name = driver.find_element(By.CSS_SELECTOR, '[data-test-id="text-user-name"]')
        log_in_button = driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-submit-login"]')

        print(user_name.text)

        user_name.click()

        logout_button = driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-handle-logout"]')

        logout_button.click()

        time.sleep(4)


        if presence_of_element_located(log_in_button):
            print('Successfully logged out')
        else:
            print('Error')

        driver.quit()



