﻿# -*- coding: utf-8 -*-
import os
import sys
import keyboard
import linecache
from tkinter import E
from time import sleep
from asyncio import log
from pathlib import Path
import unittest, time, re 
from colorama import init
from selenium import webdriver
from colorama import Fore, Back, Style
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import JavascriptException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException

# ChromiumService + ChromiumOptions
s = Service('C:\\chromedriver\\chromedriver.exe')
options = webdriver.ChromeOptions() 

# if you authorized somewhere, then launch browser with your user session (just close your Chrome)
options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data')

# removing extra traceback
sys.tracebacklimit = 0

# use Colorama to make Termcolor work on Windows too
init (autoreset = True) 

class BuyLeads(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=s, options=options)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
        # for so many seconds, he searches for the HTML element
        self.driver.implicitly_wait(4) # implicit expectation
        
        # for so many seconds, he searches for the HTML element
        self.wait = WebDriverWait(self.driver, 4) # explicit expectation
        
    # function for printing filename, linenumber, line itself, 
    # exceptions descriptions (if suddenly will be exceptions)
    def PrintException(self):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        # print("")
        print('EXCEPTION IN: =>\nPATH / FILE: {} =>\nLINE NUMBER: {} =>\nVARIABLE / ELEMENT: {}'.format(filename, lineno, line.strip()))
        
    # function used for checking is there element on page
    def check_exists_by_xpath(self, xpath):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except (NoSuchElementException, TimeoutException) as e: return False
        return True
    
    def test_buy_leads(self):
        try:
            # driver-driver
            driver = self.driver
            
            # var for exit
            exit_1 = False
            
            driver = self.driver
            # Go to the page to buy leads
            driver.get("https://advert.apileads.tech/lead/")
            time.sleep(1)
            
            while 1==1:
                try:
                    authorization = driver.find_element(By.XPATH,"//*[contains(text(),'Авторизация')]")
                    break
                except NoSuchElementException:
                    pass

                    # brand selection
                    N = 12  # number of times you want to press - [TAB]
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
                    time.sleep(1)     
                    break

            # Vertical
            Select(driver.find_element(By.ID,"leads_leadType")).select_by_visible_text("General")
            button = driver.find_element(By.XPATH,"//button[@value='0']")
            driver.execute_script("arguments[0].click();", button)
            time.sleep(1)

            # Language selection
            Select(driver.find_element(By.ID,"leads_lang")).select_by_visible_text("English")

            # 0-limits
            Select(driver.find_element(By.ID,"leads_limit_0_geo")).select_by_visible_text("Australia")
            driver.find_element(By.ID,"leads_limit_0_day").send_keys('12')
            driver.find_element(By.ID,"leads_limit_0_day").click()
            driver.find_element(By.ID,"leads_limit_0_day").clear()
            driver.find_element(By.ID,"leads_limit_0_day").send_keys("12")
            driver.find_element(By.ID,"leads_limit_0_total").send_keys("499")

            # 1-limits
            button12 = driver.find_element(By.XPATH,"//*[contains(text(),'Добавить страну')]")
            driver.execute_script("arguments[0].click();", button12)
            time.sleep(1)
            Select(driver.find_element(By.ID,"leads_limit_1_geo")).select_by_visible_text("United kingdom")
            driver.find_element(By.ID,"leads_limit_1_day").send_keys('12')
            driver.find_element(By.ID,"leads_limit_1_total").send_keys("499")

            # 2-limits
            driver.execute_script("arguments[0].click();", button12)
            time.sleep(1)
            Select(driver.find_element(By.ID,"leads_limit_2_geo")).select_by_visible_text("United states of america")
            driver.find_element(By.ID,"leads_limit_2_day").send_keys('12')
            driver.find_element(By.ID,"leads_limit_2_total").send_keys("499")

            # Start date and time zone of the advert
            driver.find_element(By.ID,"leads_sendStartAt").send_keys("12.03.2022")
            Select(driver.find_element(By.ID,"leads_timezone")).select_by_visible_text("UTC+05:00")

            # A table with a time schedule
            button1 = driver.find_element(By.XPATH,"//form[@name='leads']/descendant::td[text()='ПН']")
            driver.execute_script("arguments[0].click();", button1)
            button2 = driver.find_element(By.XPATH,"//form[@name='leads']/descendant::td[text()='ВТ']")
            driver.execute_script("arguments[0].click();", button2)
            button3 = driver.find_element(By.XPATH,"//form[@name='leads']/descendant::td[text()='СР']")
            driver.execute_script("arguments[0].click();", button3)
            button4 = driver.find_element(By.XPATH,"//form[@name='leads']/descendant::td[text()='ЧТ']")
            driver.execute_script("arguments[0].click();", button4)
            button5 = driver.find_element(By.XPATH,"//form[@name='leads']/descendant::td[text()='ПТ']")
            driver.execute_script("arguments[0].click();", button5)
            button6 = driver.find_element(By.XPATH,"//form[@name='leads']/descendant::td[text()='СБ']")
            driver.execute_script("arguments[0].click();", button6)
            button7 = driver.find_element(By.XPATH,"//form[@name='leads']/descendant::td[text()='ВС']")
            driver.execute_script("arguments[0].click();", button7)
            time.sleep(1)

            # Button to go to the second step (submit)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
            button8 = driver.find_element(By.XPATH,"//button[@type='submit']")
            driver.execute_script("arguments[0].click();", button8)

            try:
                # write script
                script = """alert(`10 - секунд вам даётся на проверку всех параметров вашего заказа!
Если что-то пошло не так, то остановите выполнение программы.`)"""
                # generate a alert via javascript
                driver.execute_script(script)
                time.sleep(10)
                ActionChains(driver).key_down(Keys.ENTER).perform()
            except UnexpectedAlertPresentException as e:
                pass

            # Button to confirm order creation (submit)
            button9 = driver.find_element(By.XPATH,"//button[contains(text(),'Подтвердить')]")
            driver.execute_script("arguments[0].click();", button9)
            time.sleep(1)

            # checking that the order has been created
            # 1 - first check
            if driver.find_element(by=By.XPATH, value="//button[contains(text(),'Оплатить')]").text == "Оплатить":
                print("----------------------------------------------------------------------")
                print("")
                print(Fore.GREEN + "1 - first check  = done! (order has been created)")
            else:
                print("")
                print(Fore.RED + "1 - first check  = error!")
        
            # 2 - second check
            while 1==1:
                
                element = self.check_exists_by_xpath("//*[contains(text(),'Заказ ID')]")

                if element is True:
                    try:
                        # write script
                        script = """alert(`Если вы нажали кнопку - [Подтвердить], то ваш заказ уже был
создан и вы видите его ID. Вам осталось только оплатить ваш
заказ, сейчас он находится в статусе: «Ожидает оплаты».`)"""
                        # generate a alert via javascript
                        driver.execute_script(script)
                        time.sleep(10)
                        ActionChains(driver).key_down(Keys.ENTER).perform()
                    except UnexpectedAlertPresentException as e:
                        pass
                    print("")
                    print(Fore.GREEN + "2 - second check = done! (order has been created)")
                    break
                else:
                    print("")
                    print(Fore.RED + "2 - second check = error!")
                    break

            # switching payment
            button10 = driver.find_element(By.ID,"advert_order_payment_payment_0")
            driver.execute_script("arguments[0].click();", button10)
            time.sleep(1)

            # Button for order payment
            button11 = driver.find_element(By.XPATH,"//button[contains(text(),'Оплатить')]")
            driver.execute_script("arguments[0].click();", button11)
            time.sleep(3)

            # all the necessary checks are on the last page (order payment verification)
            # 3 - third check
            if driver.find_element(by=By.XPATH, value="//*[contains(text(),'Заказ оплачен')]").text == "Заказ оплачен":
                print("")
                print(Fore.GREEN + "3 - third check  = done! (order is paid)")
            else:
                print("")
                print(Fore.RED + "3 - third check  = error!")
        
            # 4 - fourth check
            while 1==1:
                
                element = self.check_exists_by_xpath("//*[contains(text(),'Заказ оплачен')]")

                if element is True:
                    try:
                        # write script
                        script = "alert('Ваш заказан был успешно вами оплачен и сейчас он находится в статусе: «Активный».')"
                        # generate a alert via javascript
                        driver.execute_script(script)
                        time.sleep(8)
                        ActionChains(driver).key_down(Keys.ENTER).perform()
                    except UnexpectedAlertPresentException as e:
                        pass
                    print("")
                    print(Fore.GREEN + "4 - fourth check = done! (order is paid)")
                    break
                else:
                    print("")
                    print(Fore.RED + "4 - fourth check = error!")
                    break
                
        # catch.. catch.. catch..
        ################################################################################################################################################################################
        except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, JavascriptException, TimeoutException, ElementNotInteractableException) as ex:
            try:
                # write script
                script = "alert('Error! The requested HTML-element was not found on the HTML-page!')"
                # generate a alert via javascript
                driver.execute_script(script)
                time.sleep(5)
                ActionChains(driver).key_down(Keys.ENTER).perform()
            except UnexpectedAlertPresentException as e:
                pass
            print("----------------------------------------------------------------------")
            print(Fore.RED + "Error! The requested HTML-element was not found on the HTML-page!")
            print(Fore.RESET + "")
            self.PrintException()
            print("")
            ex_type, ex_value, ex_traceback = sys.exc_info()
            print("Exception type: %s" %ex_type.__name__)
            print("")
            print(f"Exception message: {ex.msg}")
            # print("")
            # log.logger.exception(f"Exception message: {ex.msg}", exc_info=False)
            
            # for (.bat) file start / or alternative
            print("----------------------------------------------------------------------") 
            print("TEST FAILED (requested element was not found on page)") 
            exit_1 = True 
            self.tearDown()
            
            # to see how test falls
            # sys.exit()
        ################################################################################################################################################################################
        # ENDING (script execution)
        
        # exit-exit
        if exit_1 == True:
            os._exit(0)
        
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

