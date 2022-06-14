# -*- coding: utf-8 -*-
from dataclasses import field
import sys
import random
from tkinter import E
import keyboard
from time import sleep
from pathlib import Path
import unittest, time, re 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException 
from selenium.common.exceptions import NoAlertPresentException 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException

def exception_handler(exception_type, exception, traceback):
    # All your trace are belong to us!
    # your format
    print(exception_type.__name__, exception)

sys.excepthook = exception_handler

# all variables
options = webdriver.ChromeOptions() 
options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data')
s = Service('C:\\chromedriver\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
driver.implicitly_wait(2) # for so many seconds, he searches for the HTML element
base_url = "https://www.google.com/"
verificationErrors = []
accept_next_alert = True
wait = WebDriverWait(driver, 10)

n = ['Alejandro','Ariel','Ignatius','Louis','Miguel','Pedro','Francisco','Gunnar','Bjorn','Ulf','Fyalar','Musasi','Takeshi','Yasuharu']
l = ['Aksenov','Frolov','Tretyakov','Panov','Belousov','Abramov','Voronov','Saveliev','Yudin','Kabanov','Kalashnikov','Nikonov','Bulls']

# all values these variables will change
land = str("test11-99") # land - title/name 
funnel = str("https://qazb6fe.xyz/")
name = random.choice(n)
lastname = random.choice(l)
# email = str("test-test13500+8@mail.com") # sometimes it can be used
email = 'test-test+' + (str(random.randint(10000, 99999))) + '+@gmail.com'
phone = str(random.randint(1, 9999999999)) # attention ten digits are used
# phone = str("9634706004") # sometimes it can be used
# ↑ - check error on the next test, leave old phone here

try:

    def check_exists_by_xpath(xpath):
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except (NoSuchElementException, TimeoutException) as e: return False
        return True

    ##################################################################################################
    # START
    
    # new land page
    driver.get("https://admin.apileads.tech/land/new")
    time.sleep(1)

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

    # Title + Name
    driver.find_element(By.ID,"land_form_title").send_keys(land)
    driver.find_element(By.ID,"land_form_title").click()
    driver.find_element(By.ID,"land_form_title").clear()
    driver.find_element(By.ID,"land_form_title").send_keys(land)
    time.sleep(2)
    driver.find_element(By.ID,"land_form_name").send_keys(land)
    time.sleep(2)

    # button - [Save](submit)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    saveBtn = driver.find_element(By.XPATH,"//button[@type='submit']")
    driver.execute_script("arguments[0].click();", saveBtn)
    time.sleep(2)

    # 1 - first check  
    if driver.find_element(by=By.XPATH, value=f"//*[.='{land}']").text == land:
        print("1 - first check = done! (landing page created)")
    else:
        print("1 - first check = error! (landing page not found)")
   
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
            print("2 - second check = done! (landing page created)")
            break
        else:
            print("2 - second check = error! (landing page not found)")
            break 
    # END
    ##################################################################################################
    # START

    # transition to funnel
    driver.get(funnel)
    time.sleep(2)

    # Use if the page scale is 100%
    # actions = ActionChains(driver) 
    # actions.send_keys(Keys.ARROW_DOWN * 4)
    # actions.perform()
    # time.sleep(2)
        
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

    # fill in fields
    driver.find_element(By.ID,"name").send_keys(name)
    time.sleep(2)
    driver.find_element(By.ID,"lastname").send_keys(lastname)
    time.sleep(2)
    driver.find_element(By.ID,"email").send_keys(email)
    time.sleep(2)
    driver.find_element(By.ID,"phone").send_keys(phone)
    time.sleep(2)

    # button - [...] (submit)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    submitBtn = driver.find_element(By.NAME,"submitBtn")
    driver.execute_script("arguments[0].click();", submitBtn)
    time.sleep(4)

    # END
    ##################################################################################################
    # START

    # go to page with table of all leads (apileads)
    driver.get("https://admin.apileads.tech/lead/")
    time.sleep(2)

    # field - [email]
    driver.find_element(By.ID,"lead_filter_email").send_keys(email)
    time.sleep(2)
    
    # button - [Search] (submit)  
    searchBtn = driver.find_element(By.XPATH,"//button[contains(text(),'Искать')]")
    driver.execute_script("arguments[0].click();", searchBtn)
    time.sleep(2)

    # || key - [Enter] (event is linked to it)
    # ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
    # time.sleep(1)

    # delete email from field
    driver.find_element(By.ID,"lead_filter_email").click()
    driver.find_element(By.ID,"lead_filter_email").clear()
    time.sleep(4)

    # 3 - third check  
    if driver.find_element(by=By.XPATH, value=f"//*[.='{email}']").text == email:
        print("3 - third check = done! (lead was entered into DB)")
    else:
        print("3 - third check = error! (lead not found in DB)")
   
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
            print("4 - fourth check = done! (lead was entered into DB)")
            break
        else:
            print("4 - fourth check = error! (lead not found in DB)")
            break 

    # Additional verification that there is only one such lead has been (important!!!) 
    if driver.find_element(by=By.XPATH, value="//div[@class='card-body']/child::div").text == 'Найдено лидов: 1':
        print("Additional verification. Success! There is only one such lead in the DB!")
    else:
        print("Attention! Check this email =", email)
        print("Additional verification. Error! The lead with such an email is not the only one in the DB!")

    # END
    ##################################################################################################

except (NoSuchElementException, TimeoutException):
    try:
        # write script
        script = "alert('Error! The requested element was not found on the HTML-page!')"
        # generate a alert via javascript
        driver.execute_script(script)
        time.sleep(4)
        ActionChains(driver).key_down(Keys.ENTER).perform()
    except UnexpectedAlertPresentException as e:
        pass
    print("")
    print("Error! The requested element was not found on the HTML-page!")

print("")
print("What values were used:")
print("land     =", land) 
print("funnel   =", funnel)
print("name     =", name)
print("lastname =", lastname)
print("email    =", email)
print("phone    =", phone)
driver.close()
driver.quit()