# -*- coding: utf-8 -*-
from asyncio import log
import linecache
import sys
import os
import traceback
from time import sleep
import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import JavascriptException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import WebDriverException

# ChromiumOptions
options = webdriver.ChromeOptions()

# if you authorized somewhere, then launch browser with your user session (just close your Chrome)
options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data')

# seller name (часто будет меняться)
seller = str("официальный дилер NISSAN")

# removing extra traceback
sys.tracebacklimit = 0

class ProductStore(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe", options=options) 
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
        # неявное ожидание (когда страница ещё только загружается и элемента на ней может ещё не быть)
        self.driver.implicitly_wait(2)
        
        # явное ожидание (когда нужно дождаться выполнения неких условий прежде чем идти дальше)
        self.wait = WebDriverWait(self.driver, 2, 0.2)
      
    def runTest(self):
        repeat = 5
        for i in range(repeat):
            try:
                # driver-driver
                driver = self.driver
            
                # goes to the basket
                driver.get('https://www.ozon.ru/cart')
                
                # сhecking the title of the basket
                self.assertEqual(self.driver.title,'OZON.ru - Моя корзина')
                
                # the statement that the product is in the basket
                self.assertTrue(self.is_element_present(By.XPATH,f"//*[contains(text(),'{seller}')]"))
                
                # button-1
                del_1 = str("//*[contains(text(),'Удалить выбранные')]")

                # button-2
                del_2 = str("//span[@style='border-radius: 8px;']/span[text()='Удалить']")
                
                # checks if there is + presses button - [delete ALL] (opens modal window)
                self.assertTrue(self.is_element_present(By.XPATH, del_1))
                delete_ALL = self.wait.until(EC.presence_of_element_located((By.XPATH, del_1))).click()

                # checks if there is + presses button - [delete] (removes all products and counter)
                self.assertTrue(self.is_element_present(By.XPATH, del_2))
                delete_2 = driver.find_element(By.XPATH, del_2).click()
                
                # delete_2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, del_2))).click()
                
                # checking that the basket is empty
                self.assertTrue(self.is_element_present(By.XPATH,"//h1[text()='Корзина пуста']"))
                
                break
            except WebDriverException:
                pass
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    unittest.main()