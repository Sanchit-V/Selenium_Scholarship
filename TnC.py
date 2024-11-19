from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import time
from new import driver_class
driver=driver_class.driver

class Terms_and_Conditions:
    def __init__(self):
        checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
        y_position = checkbox.location['y']

        current_position = 0
        step = 100

        while current_position < y_position:
            driver.execute_script(f"window.scrollTo(0, {current_position});")
            current_position += step
            time.sleep(0.05)

        checkbox.click()

