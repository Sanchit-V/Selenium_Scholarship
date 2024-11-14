from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from new import driver_class
driver = driver_class.driver

class has_children:
    def __init__(self):
        if driver_class.has_children == 1:

            driver.find_element(By.CSS_SELECTOR,'[data-test-id="radio-input-personal-has-children-YES"]').click()

            one_four=driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-0-4"]')
            one_four.click()
            one_four.send_keys(Keys.CONTROL + "a")
            one_four.send_keys(Keys.DELETE)
            one_four.send_keys(driver_class.number_of_children_a)

            five_twelve=driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-5-12"]')
            five_twelve.click()
            five_twelve.send_keys(Keys.CONTROL + "a")
            five_twelve.send_keys(Keys.DELETE)
            five_twelve.send_keys(driver_class.number_of_children_b)

            thirteen_eighteen=driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-13-18"]')
            thirteen_eighteen.click()
            thirteen_eighteen.send_keys(Keys.CONTROL + "a")
            thirteen_eighteen.send_keys(Keys.DELETE)
            thirteen_eighteen.send_keys(driver_class.number_of_children_c)

            eighteen_above=driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-age-range-+18"]')
            eighteen_above.click()
            eighteen_above.send_keys(Keys.CONTROL + "a")
            eighteen_above.send_keys(Keys.DELETE)
            eighteen_above.send_keys(driver_class.number_of_children_d)

        else:
            driver.find_element(By.CSS_SELECTOR,'[data-test-id="radio-input-personal-has-children-NO"]').click()

        time.sleep(2)