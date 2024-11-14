from calendar import month
from enum import CONFORM

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
import time
from new import driver_class
driver = driver_class.driver
monthly_Income=driver_class.Monthly_income
monthly_Expense=driver_class.Monthly_expense

class income_expense:
    def __init__(self):
        monthly_income=driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-monthly-income"]')
        monthly_income.click()
        monthly_income.send_keys(Keys.CONTROL + "a")
        monthly_income.send_keys(Keys.DELETE)
        time.sleep(2)
        monthly_income.send_keys(monthly_Income)

        monthly_expense=driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-personal-monthly-expense"]')
        monthly_expense.click()
        monthly_expense.send_keys(Keys.CONTROL + "a")
        monthly_expense.send_keys(Keys.DELETE)
        time.sleep(2)
        monthly_expense.send_keys(monthly_Expense)


class financially_independent:
    def __init__(self):
        if financially_independent == 1:
            driver.find_element(By.CSS_SELECTOR,'[data-test-id="radio-input-personal-financially-dependent-YES"]').click()

        else:
            driver.find_element(By.CSS_SELECTOR,'[data-test-id="radio-input-personal-financially-dependent-NO"]').click()