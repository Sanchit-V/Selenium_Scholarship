from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from new import driver_class
from login_page import login_page
from new import driver_class
from personal_details import personal_details
from welcompage import welcomepage
from welcompage import  Logged_in_toast
from birth_details import birth_details,nation,state,city,nationality
from income_expense import income_expense,financially_independent
from children_details import has_children
language=driver_class.language



driver=driver_class.driver
pass_key=driver_class.pass_key
driver.get('http://localhost:3000')
driver.maximize_window()
time.sleep(5)

def test_Language_Button_Click():
    driver.find_element(By.CSS_SELECTOR, '[data-test-id="select-language"]').click()
    time.sleep(1)

def test_Login_page():
    login_page()
def test_Welcome_page():
    welcomepage()
def test_login_toast():
    Logged_in_toast()
def test_get_started_button():
    driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-get-started-welcome"]').click()
    time.sleep(2)
def test_Personal_Details():
    personal_details()
def test_Birth_Details():
    birth_details()
def test_Nation():
    nation()
def test_State():
    state()
def test_City():
    city()
def test_Nationality():
    nationality()
def test_Income_Expense():
    income_expense()
def test_Financially_Independent():
    financially_independent()
def test_Has_Children():
    has_children()
def test_Personal_Details_Continue_Button():
    driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-continue-personal"]').click()
    time.sleep(4)




































    







