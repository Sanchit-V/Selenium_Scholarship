from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time



class driver_class:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    pass_key = '7ccf20e'
    language = 1 #put 1 for english and 0 for spanish
    country ='India'
    state ='Bihar'
    city ='Patna'
    nationality ='India'

    financially_independent = 1 #put 1 for independent and 0 for dependent

    has_children = 1  # put 1 for children and 0 for no children

    # children_category= 'a' #a(0-4) #b(5-12) #c(13-18) #d(18+)
    number_of_children_a = 2  # pre-specify the number in a
    number_of_children_b = 3  # pre-specify the number in b
    number_of_children_c = 1  # pre-specify the number in c
    number_of_children_d = 5  # pre-specify the number in d



