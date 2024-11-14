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







print(email_Ids)


class default_email:
    def __init__(self):
        default=driver_class.driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-default-email"]')

        if presence_of_element_located(default):
            print("Default email is present.")
        else:
            print("Error")



class Email:
    def __init__(self):

        for email in range(number_of_Emails):


            add_email = driver_class.driver.find_element(By.CSS_SELECTOR,'[data-test-id="text-address-contact-email-add"]')
            add_email.click()
            time.sleep(1)




        if number_of_Emails == 1:
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').send_keys(Keys.DELETE)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').send_keys(email_Ids[0])

        elif number_of_Emails == 2:
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').send_keys(Keys.DELETE)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').send_keys(email_Ids[0])
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').send_keys(Keys.DELETE)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').send_keys(email_Ids[1])

        elif number_of_Emails == 3:
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').send_keys(Keys.DELETE)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').send_keys(email_Ids[0])
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').send_keys(Keys.DELETE)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').send_keys(email_Ids[1])
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-2"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-2"]').send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-2"]').send_keys(Keys.DELETE)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-2"]').send_keys(email_Ids[2])

        elif number_of_Emails == 4:
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').send_keys(Keys.DELETE)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').send_keys(email_Ids[0])
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').send_keys(Keys.DELETE)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').send_keys(email_Ids[1])
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-2"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-2"]').send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-2"]').send_keys(Keys.DELETE)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-2"]').send_keys(email_Ids[2])
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-3"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-3"]').send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-3"]').send_keys(Keys.DELETE)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-3"]').send_keys(email_Ids[3])

        elif number_of_Emails == 5:
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').send_keys(Keys.DELETE)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-0"]').send_keys(email_Ids[0])
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').send_keys(Keys.DELETE)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-1"]').send_keys(email_Ids[1])
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-2"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-2"]').send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-2"]').send_keys(Keys.DELETE)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-2"]').send_keys(email_Ids[2])
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-3"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-3"]').send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-3"]').send_keys(Keys.DELETE)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-3"]').send_keys(email_Ids[3])
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-4"]').click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-4"]').send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-4"]').send_keys(Keys.DELETE)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-email-4"]').send_keys(email_Ids[4])

        else:
            print("No additional mails added, just default is present")

class def_Phone_number:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-0"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-0"]').send_keys(Keys.CONTROL+'a')
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-0"]').send_keys(Keys.DELETE)
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-0"]').send_keys(Def_phone)
        time.sleep(2)

class def_Whatsapp_number:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-1"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-1"]').send_keys(Keys.CONTROL+'a')
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-1"]').send_keys(Keys.DELETE)
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-1"]').send_keys(Def_whatsapp)
        time.sleep(2)

class additional_contact:
    def __init__(self):
        for addition_Contact_phone in range (add_phone):
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="text-address-contact-add-phone-number"]').click()
            driver.find_element(By.XPATH, "//input[@value='phone']").click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-dialog-confirm-add-number"]').click()

time.sleep(2)

class additional_whatsapp:
    def __init__(self):
        for additional_whatsapp_phone in range (add_whatsapp):
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="text-address-contact-add-phone-number"]').click()
            driver.find_element(By.XPATH, "//input[@value='whatsapp']").click()
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="btn-dialog-confirm-add-number"]').click()

time.sleep(2)

class country_code:
    def __init__(self):


        driver.find_element(By.CSS_SELECTOR, '[data-test-id="text-country-phone-code-0"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(country_Code)
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(random.choice(country_Code))
        time.sleep(2)

        if country_Code == 'India':
            for i in range (2):
                driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.ARROW_DOWN)

            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.RETURN)

        else:
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.RETURN)




        driver.find_element(By.CSS_SELECTOR, '[data-test-id="text-country-phone-code-1"]').click()
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(random.choice(country_Code))
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(country_Code)
        time.sleep(2)

        if country_Code == 'India':
            for i in range(2):
                driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.ARROW_DOWN)

            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.RETURN)

        else:
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.RETURN)



        driver.find_element(By.CSS_SELECTOR, '[data-test-id="text-country-phone-code-2"]').click()
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(random.choice(country_Code))
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(country_Code)
        time.sleep(2)

        if country_Code == 'India':
            for i in range(2):
                driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.ARROW_DOWN)

            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.RETURN)

        else:
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.RETURN)



        driver.find_element(By.CSS_SELECTOR, '[data-test-id="text-country-phone-code-3"]').click()
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(random.choice(country_Code))
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(country_Code)
        time.sleep(2)

        if country_Code == 'India':
            for i in range(2):
                driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.ARROW_DOWN)

            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.RETURN)

        else:
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.RETURN)




        driver.find_element(By.CSS_SELECTOR, '[data-test-id="text-country-phone-code-4"]').click()
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(random.choice(country_Code))
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(country_Code)
        time.sleep(2)

        if country_Code == 'India':
            for i in range(2):
                driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.ARROW_DOWN)

            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.RETURN)

        else:
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-filter-flag"]').send_keys(Keys.RETURN)

        #country_code_options = driver.find_elements(By.XPATH, "//div[@class='MuiAutocomplete-popper MuiBox-root css-1mtsuo7']")

        #for option in country_code_options:
           # option_country=option.text.strip()
            #print(option_country)
            #if option_country == country_Code:
               # option.click()
            #else:
                #print('not found')
               # break

        time.sleep(1)

class enter_phone_number:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-2"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-2"]').send_keys(driver_class.additional_1)

        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-3"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-3"]').send_keys(driver_class.additional_2)

        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-4"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-address-contact-phone-number-4"]').send_keys(driver_class.additional_3)

        time.sleep(2)







class address_nationality:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="autocomplete-input-addresses-residence-country"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="autocomplete-input-addresses-residence-country"]').send_keys(driver_class.country_code)
        time.sleep(2)

        if country_Code == 'India':
            for i in range (2):
                driver.find_element(By.CSS_SELECTOR, '[data-test-id="autocomplete-input-addresses-residence-country"]').send_keys(Keys.ARROW_DOWN)

            time.sleep(1)

            driver.find_element(By.CSS_SELECTOR, '[data-test-id="autocomplete-input-addresses-residence-country"]').send_keys(Keys.ENTER)

        else:
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="autocomplete-input-addresses-residence-country"]').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.CSS_SELECTOR, '[data-test-id="autocomplete-input-addresses-residence-country"]').send_keys(Keys.ENTER)




        try :
            home_State = driver.find_element(By.CSS_SELECTOR,'[data-test-id="autocomplete-input-addresses-residence-state"]')
            home_State.click()
            print('Web Element found')
            home_State.send_keys(driver_class.Home_State)
            home_State.send_keys(Keys.ARROW_DOWN)
            home_State.send_keys(Keys.ENTER)
        except:
            print('No State')


        time.sleep(2)

        try:
            home_City = driver.find_element(By.CSS_SELECTOR,'[data-test-id="autocomplete-input-addresses-residence-city"]')
            home_City.click()
            print('Web Element found')
            home_City.send_keys(driver_class.Home_city)
            home_City.send_keys(Keys.ARROW_DOWN)
            home_City.send_keys(Keys.ENTER)
        except:
            print('No City')






    time.sleep(6)


    time.sleep(2)

        #Address_nationality=driver.find_elements(By.XPATH, "//input[@id='combo-box-demo']")

        #for option in Address_nationality:
            #Address_nation=option.text.strip()
            #if Address_nation == country_Code:
                #option.click()
            #else:
                #print('not found')
                #break

        #time.sleep(1)





class Housing_type:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="select-display-addresses-residence-type-of-housing"]').click()

        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-addresses-residence-type-of-housing-Department"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-addresses-residence-type-of-housing-House"]').click()

        time.sleep(3)

class Housing_conditions:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="select-display-addresses-residence-housing-condition"]').click()

        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-addresses-residence-housing-condition-Family"]').click()
        #driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-addresses-residence-housing-condition-Own"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="li-addresses-residence-housing-condition-Rented"]').click()

        time.sleep(3)

class Zip_code:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-addresses-residence-zip-code"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-addresses-residence-zip-code"]').send_keys('QW12142W')

class home_Address:
    def __init__(self):
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-addresses-residence-address"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test-id="input-addresses-residence-address"]').send_keys(driver_class.home_address)

        time.sleep(3)


















































