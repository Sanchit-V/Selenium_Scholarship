from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from new import driver_class

driver = driver_class.driver
Date = driver_class.date
Country = driver_class.country
State = driver_class.state
City = driver_class.city
Nationality = driver_class.nationality

class birth_details:
    def __init__(self):
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="date-picker-input-personal-birth-date"]').clear()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="date-picker-input-personal-birth-date"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="date-picker-input-personal-birth-date"]').send_keys(Date)
        time.sleep(3)



class nation:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="autocomplete-input-personal-birth-country"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="autocomplete-input-personal-birth-country"]').send_keys(Country)
        time.sleep(2)
        nation_options = driver.find_elements(By.CSS_SELECTOR, '#combo-box-demo-listbox li')
        for option in nation_options:
            option_text = option.text.strip()
            if option_text == Country:
                option.click()
                break

        time.sleep(1)


class state:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="autocomplete-input-personal-birth-state"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="autocomplete-input-personal-birth-state"]').send_keys(State)
        time.sleep(2)

        state_options = driver.find_elements(By.CSS_SELECTOR, '#combo-box-demo-listbox li')
        for option in state_options:
            option_text = option.text.strip()
            if option_text == State:
                option.click()
                break

        time.sleep(1)

class city:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="autocomplete-input-personal-birth-city"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="autocomplete-input-personal-birth-city"]').send_keys(City)
        time.sleep(2)

        city_options = driver.find_elements(By.CSS_SELECTOR, '#combo-box-demo-listbox li')
        for option in city_options:
            option_text = option.text.strip()
            if option_text == City:
                option.click()
                break

        time.sleep(1)


class nationality:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="autocomplete-input-personal-birth-nationality"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="autocomplete-input-personal-birth-nationality"]').send_keys(Nationality)
        time.sleep(2)

        nationality_options = driver.find_elements(By.CSS_SELECTOR, '#combo-box-demo-listbox li')
        for option in nationality_options:
            option_text = option.text.strip()
            if option_text == Nationality:
                option.click()
                break

        time.sleep(1)

