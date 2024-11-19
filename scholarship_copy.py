from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time

from additional_info import add_info
from new import driver_class
from login_page import login_page
from new import driver_class
from personal_details import personal_details
from welcompage import welcomepage
from welcompage import  Logged_in_toast
from birth_details import birth_details,nation,state,city,nationality
from income_expense import income_expense,financially_independent
from children_details import has_children
from client_contact import Email, default_email, def_Phone_number, def_Whatsapp_number, additional_contact, \
    additional_whatsapp, country_code, address_nationality, Housing_type, enter_phone_number, Housing_conditions, \
    Zip_code, home_Address
from TnC import Terms_and_Conditions
from logout_username import Logout_username
from cancel_button import Cancel_button_Personal, Cancel_button_Address, Cancel_button_Additional, Accept_Cancel, \
    Decline_Cancel
from back_button import Back_Button_Address, Back_Button_Additional

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

#def test_account_details_with_logout():
    #Logout_username()








#def test_back_button():
    #driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-back-address"]').click()


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
    time.sleep(4)

def test_cancel_functionality_personal():
    Cancel_button_Personal()
    time.sleep(2)
    # Cancel_button_Address()
    # Cancel_button_Additional()
    #Accept_Cancel()
    time.sleep(2)
    Decline_Cancel()

def test_Income_Expense():
    income_expense()
def test_Financially_Independent():
    financially_independent()
def test_Has_Children():
    has_children()
def test_Personal_Details_Continue_Button():
    driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-continue-personal"]').click()
    time.sleep(4)
def test_default_Email():
    default_email()

time.sleep(3)

#def test_back_button_address():
    #Back_Button_Address()

def test_add_Email():
    Email()
    time.sleep(2)

def test_Phone_number_def():
    def_Phone_number()

def test_Whatsapp_number_def():
    def_Whatsapp_number()



def test_cancel_functionality_address():
    #Cancel_button_Personal()
    Cancel_button_Address()
    time.sleep(2)
    # Cancel_button_Additional()
    #Accept_Cancel()
    time.sleep(2)
    Decline_Cancel()

def test_additional_phone():
    additional_contact()

def test_additional_whatsapp():
    additional_whatsapp()

def test_country_code():
    country_code()

def test_address_Nationality():
    address_nationality()

def test_housing_type():
    Housing_type()

def test_additional_contact():
    enter_phone_number()

def test_housing_conditions():
    Housing_conditions()

def test_Zip_code():
    Zip_code()

def test_home_address():
    home_Address()

def test_continue_button_2():
    driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-continue-address"]').click()
    time.sleep(4)

def test_additional_back_button():
    Back_Button_Additional()

def test_cancel_functionality_additional():
    # Cancel_button_Personal()
    # Cancel_button_Address()
    Cancel_button_Additional()
    time.sleep(2)
    #Accept_Cancel()
    time.sleep(2)
    Decline_Cancel()

def test_additional_info_page():
    add_info()



def test_finalize_button():
    driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-continue-additional"]').click()

    time.sleep(7)

def test_check_button_tnc():

    Terms_and_Conditions()

    driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-send-summary"]').click()

    time.sleep(5)

def test_form_submitted():
    submitted_message=driver.find_element(By.CSS_SELECTOR, '[data-test-id="text-submitted-title"]').text
    print('\t')
    print('*****************************************\t')
    if 'Form Submission Successful' in submitted_message:
        print('Form Submitted')

    else:
        'No submission.'


    print('*****************************************\t')

    time.sleep(2)











































    







