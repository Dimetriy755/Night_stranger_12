# -*- coding: utf-8 -*-
import linecache
import os
import sys
import random
import keyboard
from tkinter import E
from time import sleep
from pathlib import Path
import unittest, time, re 
from dataclasses import field
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import NoAlertPresentException 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException

# ChromiumService + ChromiumOptions
s = Service('C:\\chromedriver\\chromedriver.exe')
options = webdriver.ChromeOptions() 

# if you authorized somewhere, then launch browser with your user session (just close your Chrome)
options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data')

# all necessary variables
base_url = "https://www.google.com/"
driver = webdriver.Chrome(service=s, options=options)

# removing extra traceback
sys.tracebacklimit = 0

# for so many seconds, he searches for the HTML-element
driver.implicitly_wait(3) # implicit expectation

# for so many seconds, he searches for the HTML-element
wait = WebDriverWait(driver, 3) # explicit expectation

# var for exit
exit_1 = False

# lists of names and lastnames
n = ['Alejandro','Ariel','Ignatius','Louis','Miguel','Pedro','Francisco','Gunnar','Bjorn','Ulf','Fyalar','Musasi','Takeshi','Yasuharu']
l = ['Aksenov','Frolov','Tretyakov','Panov','Belousov','Abramov','Voronov','Saveliev','Yudin','Kabanov','Kalashnikov','Nikonov','Bulls']

# all values these variables will be change
land = str("test11-99") # land - title/name 
funnel = str("https://qazb6fe.xyz/")
name = random.choice(n)
lastname = random.choice(l)
# email = str("test-test13500+8@mail.com") # sometimes it can be used
email = 'test-test+' + (str(random.randint(10000, 99999))) + '+@gmail.com'
phone = str(random.randint(1, 9999999999)) # attention ten digits are used
# phone = str("9634706004") # sometimes it can be used
# ↑ - check error on the next test, leave old phone here

# function for printing filename, linenumber, line itself, 
# exceptions descriptions (if suddenly will be exceptions)
def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print("")
    print('EXCEPTION IN: =>\nPATH / FILE: {} =>\nLINE NUMBER: {} =>\nVARIABLE / ELEMENT: {}'.format(filename, lineno, line.strip()))
    
# function used for checking is there element on page
def check_exists_by_xpath(xpath):
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    except (NoSuchElementException, TimeoutException) as e: return False
    return True
    
try:
##################################################################################################
# START (creating new landing page (her entitys in DB via web UI))
    
    # new land page
    driver.get("https://admin.apileads.tech/land/new")
    time.sleep(1)
    
    while 1==1:
        try:
            authorization = driver.find_element(By.XPATH,"//*[contains(text(),'Авторизация')]")
            break
        except NoSuchElementException:
            pass

            # Offer selection
            N = 25  # number of times you want to press - [TAB]
            actions = ActionChains(driver)
            for _ in range(N):
                actions = actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(1)
            ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
            time.sleep(1)
            ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
            time.sleep(1)
            ActionChains(driver).key_down(Keys.ENTER).perform()
            time.sleep(2)         
            break

    # Title + Name
    driver.find_element(By.ID,"land_form_title").send_keys(land)
    driver.find_element(By.ID,"land_form_title").click()
    driver.find_element(By.ID,"land_form_title").clear()
    driver.find_element(By.ID,"land_form_title").send_keys(land)
    time.sleep(2)
    driver.find_element(By.ID,"land_form_name").send_keys(land)
    time.sleep(2)

    # presses button - [Save](submit)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    saveBtn = driver.find_element(By.XPATH,"//button[@type='submit']")
    driver.execute_script("arguments[0].click();", saveBtn)
    time.sleep(2)

    # 1 - first check  
    if driver.find_element(by=By.XPATH, value=f"//*[.='{land}']").text == land:
        print("----------------------------------------------------------------------")
        print("")
        print("1 - first check  = done!  (landing page created)")
    else:
        print("----------------------------------------------------------------------")
        print("")
        print("1 - first check  = error! (landing page not found)")
   
    # 2 - second check
    while 1==1:
        
        element = check_exists_by_xpath(f"//*[.='{land}']")

        if element is True:
            try:
                # write script
                script = "alert('Landing page was successfully created!')"
                # generate a alert via javascript
                driver.execute_script(script)
                time.sleep(4)
                ActionChains(driver).key_down(Keys.ENTER).perform()
            except UnexpectedAlertPresentException as e:
                pass
            print("")
            print("2 - second check = done!  (landing page created)")
            break
        else:
            print("")
            print("2 - second check = error! (landing page not found)")
            break 
        
    # END (creating new landing page (her entitys in DB via web UI))
    ##################################################################################################
    # START (registration of the target lead via test funnel)

    # transition to funnel
    driver.get(funnel)
    time.sleep(2)

    # Use if your page scale is 100%
    # actions = ActionChains(driver) 
    # actions.send_keys(Keys.ARROW_DOWN * 4)
    # actions.perform()
    # time.sleep(2)
    
    # selects phone country code    
    phone_code = driver.find_element(By.CLASS_NAME,"ms-dd-header")
    driver.execute_script("arguments[0].click();", phone_code)
    time.sleep(2)
    actions = ActionChains(driver) 
    actions.send_keys(Keys.ARROW_UP * (random.randint(1, 227)))
    actions.send_keys(Keys.ARROW_DOWN * (random.randint(1, 227)))
    actions.send_keys(Keys.ARROW_UP * (random.randint(1, 227)))
    actions.perform()
    time.sleep(2)
    ActionChains(driver).key_down(Keys.ENTER).perform()
    time.sleep(2)

    # fills in all fields
    driver.find_element(By.ID,"name").send_keys(name)
    time.sleep(2)
    driver.find_element(By.ID,"lastname").send_keys(lastname)
    time.sleep(2)
    driver.find_element(By.ID,"email").send_keys(email)
    time.sleep(2)
    driver.find_element(By.ID,"phone").send_keys(phone)
    time.sleep(2)

    # presses button - [...] (submit)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    submitBtn = driver.find_element(By.NAME,"submitBtn")
    driver.execute_script("arguments[0].click();", submitBtn)
    time.sleep(4)

    # END (registration of the target lead via test funnel)
    ##################################################################################################
    # START (goes to lead page and checks that target lead already in DB)

    # go to page with table of all leads (apileads)
    driver.get("https://admin.apileads.tech/lead/")
    time.sleep(2)

    # fills in field - [email]
    driver.find_element(By.ID,"lead_filter_email").send_keys(email)
    time.sleep(2)
    
    # presses button - [Search] (submit)  
    searchBtn = driver.find_element(By.XPATH,"//button[contains(text(),'Искать')]")
    driver.execute_script("arguments[0].click();", searchBtn)
    time.sleep(2)

    # || key - [Enter] (event is linked to it)
    # ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
    # time.sleep(1)

    # deletes email from field
    driver.find_element(By.ID,"lead_filter_email").click()
    driver.find_element(By.ID,"lead_filter_email").clear()
    time.sleep(4)

    # 3 - third check  
    if driver.find_element(by=By.XPATH, value=f"//*[.='{email}']").text == email:
        print("")
        print("3 - third check  = done!  (lead was entered into DB)")
    else:
        print("")
        print("3 - third check  = error! (lead not found in DB)")
   
    # 4 - fourth check
    while 1==1:
        
        element = check_exists_by_xpath(f"//*[.='{email}']")

        if element is True:
            try:
                # write script
                script = "alert('Client email has been detected! Success!')"
                # generate a alert via javascript
                driver.execute_script(script)
                time.sleep(4)
                ActionChains(driver).key_down(Keys.ENTER).perform()
            except UnexpectedAlertPresentException as e:
                pass
            print("")
            print("4 - fourth check = done!  (lead was entered into DB)")
            print("----------------------------------------------------------------------") 
            break
        else:
            print("")
            print("4 - fourth check = error! (lead not found in DB)")
            print("----------------------------------------------------------------------") 
            break 

    # Additional verification that there is only one such lead has been (important!!!) 
    if driver.find_element(by=By.XPATH, value="//div[@class='card-body']/child::div").text == 'Найдено лидов: 1':
        print("Additional verification. Success! There is only one such lead in the DB!")
    else:
        print("Attention! Check this email =", email)
        print("Additional verification. Error! The lead with such an email is not the only one in the DB!")

# END (goes to lead page and checks that target lead already in DB)
##################################################################################################
except (NoSuchElementException, TimeoutException) as ex:
    try:
        # write script
        script = "alert('Error! The requested element was not found on the HTML-page!')"
        # generate a alert via javascript
        driver.execute_script(script)
        time.sleep(4)
        ActionChains(driver).key_down(Keys.ENTER).perform()
    except UnexpectedAlertPresentException as e:
        pass
    print("----------------------------------------------------------------------")
    print("Error! The requested element was not found on the HTML-page!")
    PrintException()
    print("")
    ex_type, ex_value, ex_traceback = sys.exc_info()
    print("Exception type: %s" %ex_type.__name__)
    print("")
    print(f"Exception message: {ex.msg}")
    print("----------------------------------------------------------------------") 
    print("TEST FAILED (requested element was not found on page)") 
    exit_1 = True
    driver.close()
    driver.quit()
    # sys.exit()
##################################################################################################
# ENDING (script execution)

# exit-exit
if exit_1 == True:
    os._exit(0)

# test data / all checks
print("")
print("")
print("What values were used:")
print("land     =", land) 
print("funnel   =", funnel)
print("name     =", name)
print("lastname =", lastname)
print("email    =", email)
print("phone    =", phone)
print("")
print("+ What was checked:") 
print("1. creating new landing page (her entitys in DB via web UI)")
print("2. registration of the target lead via test funnel (landing)")
print("3. checking that the target lead has successfully registered")
print("----------------------------------------------------------------------")

# closes window and exits driver
driver.close()
driver.quit()