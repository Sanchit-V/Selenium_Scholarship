from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time



class driver_class:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    pass_key = 'e9a7e5f'
    language = 1 #put 1 for english and 0 for spanish
    date = '02/12/2022'
    country ='India'
    state ='Haryana'
    city ='Ambala'
    nationality ='Pakistan'
    Monthly_income = "2020202"
    Monthly_expense = "11111"

    financially_independent = 1 #put 1 for independent and 0 for dependent

    has_children = 1  # put 1 for children and 0 for no children

    # children_category= 'a' #a(0-4) #b(5-12) #c(13-18) #d(18+)
    number_of_children_a = 2  # pre-specify the number in a
    number_of_children_b = 3  # pre-specify the number in b
    number_of_children_c = 1  # pre-specify the number in c
    number_of_children_d = 5  # pre-specify the number in d

    number_of_email = 2

    email_id = ["example1@gmail.com", "example2@yahoo.com", "example3@outlook.com", "example4@gmail.com", "example5@yahoo.com"]

    #for i in range (number_of_email):
       # email_field_pseudo = 'data-test-id="input-address-contact-email-'
        #d_t_id = "{}{}".format(email_field_pseudo, i)
       # print(d_t_id)
        #data_test_id.append(d_t_id)

   # print(data_test_id)

    default_phone=9800199911
    default_whatsapp=8766223432

    number_of_additional_phone=2
    number_of_additional_whatsapp=1
    #country_code=['India','Spain','Cuba', 'Pakistan', 'Italy', 'Argentina', 'Portugal']
    country_code='India'

    additional_1=7676716221
    additional_2=9088989765
    additional_3=9666777887

    home_address = "7684 Cambridge Road, Lake Noramouth, NY 12345"

    Home_country = 'India'
    Home_State = 'Punjab'
    Home_city = 'Patiala'












