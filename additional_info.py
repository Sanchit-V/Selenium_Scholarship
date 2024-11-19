import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
from new import driver_class
driver=driver_class.driver
number_of_Emails=driver_class.number_of_email
email_Ids=driver_class.email_id
Def_phone=driver_class.default_phone
Def_whatsapp=driver_class.default_whatsapp
add_phone=driver_class.number_of_additional_phone
add_whatsapp=driver_class.number_of_additional_whatsapp
country_Code=driver_class.country_code

class add_info:
    def __init__(self):
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Google"]').click()
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Facebook"]').click()
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Instagram"]').click()
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Referred"]').click()
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Company"]').click()
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Agreement"]').click()
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-University"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Speech"]').click()
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="radio-input-additional-information-knowledge-pathway-Webinar"]').click()

        time.sleep(2)

        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-additional-information-referral-details"]').click()
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-additional-information-referral-details"]').send_keys('In the end, Alex and Casey outsmarted Dr. Eveline and returned to New York as heroes, their friendship stronger than ever.')

        try:
            text_field= driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-additional-information-referral-details"]')
            print('\t')
            print('*****************************************\t')
            print('Web element found\t')
            print('*****************************************')
            text_field.click()
            text_field.send_keys('In the end, Alex and Casey outsmarted Dr. Eveline and returned to New York as heroes, their friendship stronger than ever.')

        except:
            print('No text field')
