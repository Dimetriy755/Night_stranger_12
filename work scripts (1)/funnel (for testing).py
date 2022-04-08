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

# variables
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
funnel = str("https://qazb6fe.xyz/")
name = random.choice(n)
lastname = random.choice(l)
# email = str("test32+3345@mail.com") # sometimes it can be used
email = 'test-test+' + (str(random.randint(10000, 99999))) + '+@gmail.com'
phone = str(random.randint(1, 9999999999)) # attention ten digits are used
# phone = str("1876544400") # sometimes it can be used
# ↑ - check error on the next test, leave old phone here

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
time.sleep(10)

print("What values were used:")
print("name =", name)
print("lastname =", lastname)
print("email =", email)
print("phone =", phone)

driver.close()
driver.quit()

# END
##################################################################################################