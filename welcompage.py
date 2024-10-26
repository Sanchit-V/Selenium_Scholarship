from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from new import driver_class
language=driver_class.language

class Logged_in_toast:
    def __init__(self):
        if language==1:
            logged_in_toast = driver_class.driver.find_element(By.CSS_SELECTOR,'#notistack-snackbar > .MuiTypography-root').text
            # print(logged_in_toast)

            if 'Applicant logged in' in logged_in_toast:
                print("The toast message is present")
            else:
                print("Nothing found, failed")

        else:
            logged_in_toast = driver_class.driver.find_element(By.CSS_SELECTOR,'#notistack-snackbar > .MuiTypography-root').text

            if 'El solicitante inició sesión' in logged_in_toast:
                print("The toast message is present")

            else:
                print("Nothing found, failed")



class welcomepage():
    def __init__(self):
        if language == 1:
            welcome_message = driver_class.driver.find_element(By.CSS_SELECTOR,'[data-test-id="text-welcome-message"]').text

            if 'Welcome to the online scholarship application form' in welcome_message:
                print("Passed, Welcome message present")
            else:
                print("Failed, No welcome message found.")

        else :
            welcome_message = driver_class.driver.find_element(By.CSS_SELECTOR,'[data-test-id="text-welcome-message"]').text

            if 'Bienvenido al formulario de solicitud de beca online' in welcome_message:
                print("Passed, Welcome message present")
            else:
                print("Failed, No welcome message found.")



