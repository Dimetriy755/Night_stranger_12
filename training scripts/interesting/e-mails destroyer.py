# -*- coding: utf-8 -*-
import linecache
import pyautogui
import sys
import os
import traceback
from time import sleep
import unittest, time, re
from selenium import webdriver
from pyautogui import FailSafeException
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

# ChromiumService + ChromiumOptions
# service = Service('C:\\chromedriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data')

# disable protection pyautogui
pyautogui.FAILSAFE = False

# removing extra traceback
sys.tracebacklimit = 0

# go from zero to hero
class SpamDestroy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe", options=options)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 5, 0.3) 
        
    def PrintException(self):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        # print("")
        print('EXCEPTION IN: =>\nPATH / FILE: {} =>\nLINE NUMBER: {} =>\nVARIABLE / ELEMENT: {}'.format(filename, lineno, line.strip()))
        
    def check_exists_by_xpath(self, xpath):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except (NoSuchElementException, TimeoutException) as e: return False
        return True
       
    def test_killers_email(self):
        while 1==1:
            try: 
                # exit_1 = False
                
                driver = self.driver
                driver.get("https://www.google.com/")
                driver.maximize_window()
                time.sleep(2)

                mail = driver.find_element(By.XPATH,"//a[text()='Почта']")
                mail.click()
                time.sleep(2)
                
                settings = driver.find_element(By.XPATH,"//button[@aria-label='Расширенный поиск']")
                settings.click()
                time.sleep(2)
                
                period = driver.find_element(By.XPATH,"//div[@aria-label='Период']")
                period.click()
                time.sleep(2)
            
                year_1 = driver.find_element(By.XPATH,"//div[text()='1 год']")
                year_1.click()
                time.sleep(2)
                
                search = driver.find_element(By.XPATH,"//div[@aria-label='Поиск почты']")
                search.click()
                time.sleep(2)
                
                # Здесь вот имеется странная ошибка из-за режима - [Расширенный поиск].
                # Без его включения всё отлично работает (с ним нет, но мне он нужен).
                # Exception type: ElementNotInteractableException (тип этой ошибки)
                # Exception message: element not interactable (сообщение что не так)
                # while 1==1:
                #     try:
                #         empty = driver.find_element(By.XPATH,"//tr[@class='TD']//a[@ghelpcontext='broaden_search']")
                #         driver.execute_script("arguments[0].scrollIntoView();", empty)
                #         break
                #     except NoSuchElementException:
                #         pass
                
                #         # check checkbox = [ALL] (necessary choice)
                #         checkbox = driver.find_element(By.CSS_SELECTOR,"span[style='user-select: none;']")
                #         checkbox.click()
                #         checkbox = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[style='user-select: none;']"))).click()
                #         time.sleep(2)
                        
                #         # press button - [delete] (main functionality)
                #         delete = driver.find_element(By.CSS_SELECTOR,"div[aria-label='Удалить']")
                #         delete.click()
                #         delete = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[aria-label='Удалить']"))).click()
                #         time.sleep(2) 
                #         break
            
                # И мне пришлось прибегнуть к помощи pyautogui (my experiments).
                # Однако, такой вот необычный способ здесь вот отлично работает. 
                while 1==1:
                    try:
                        empty = driver.find_element(By.XPATH,"//tr[@class='TD']//a[@ghelpcontext='broaden_search']")
                        driver.execute_script("arguments[0].scrollIntoView();", empty)
                        break
                    except NoSuchElementException:
                        pass
                    
                        # checkbox = [ALL] (necessary choice)
                        pyautogui.move(-1275, 0, duration=0.25) # left
                        time.sleep(1)

                        pyautogui.move(0, -1275, duration=0.25) # up
                        time.sleep(1)

                        pyautogui.move(300, 0, duration=0.25)  # right
                        time.sleep(2)

                        pyautogui.move(0, 254, duration=0.25)  # down
                        time.sleep(2)
                        
                        pyautogui.click(button='left') # left-click
                        time.sleep(2)
                        
                        # down + [ENTER]
                        ActionChains(driver).key_down(Keys.ARROW_DOWN).perform() 
                        time.sleep(1)
                        ActionChains(driver).key_down(Keys.ENTER).perform()
                        time.sleep(2)
                
                        # hover pointer and press button - [delete]
                        pyautogui.move(-1275, 0, duration=0.25) # left
                        time.sleep(1)

                        pyautogui.move(0, -1275, duration=0.25) # up
                        time.sleep(1)

                        pyautogui.move(425, 0, duration=0.25)  # right
                        time.sleep(2)

                        pyautogui.move(0, 254, duration=0.25)  # down
                        time.sleep(2)

                        pyautogui.click(button='left') # left-click
                        time.sleep(2)
                        break
            
                more = driver.find_element(By.XPATH,"//div[@role='navigation']//span[@role='button']//span[contains(text(),'Ещё')]")
                more.click()
                time.sleep(2)
                
                basket = driver.find_element(By.XPATH,"//div[@data-tooltip='Корзина']//a[@aria-label='Корзина']")
                driver.execute_script("arguments[0].scrollIntoView();", basket)
                driver.execute_script("arguments[0].click();", basket)
                time.sleep(2)
            
                while 1==1:
                    try:
                        clear_1 = driver.find_element(By.XPATH,"//div[@role='main']//span[contains(text(),'Очистить корзину')]")
                        clear_1.click()
                        time.sleep(2)
                        ActionChains(driver).key_down(Keys.ENTER).perform()
                        time.sleep(2)
                        break
                    except NoSuchElementException:
                        pass
                        break
            
                spam = driver.find_element(By.XPATH,"//div[@data-tooltip='Спам']//a[contains(text(),'Спам')]")
                driver.execute_script("arguments[0].click();", spam)
                time.sleep(2)
                
                while 1==1:
                    try:
                        clear_2 = driver.find_element(By.XPATH,"//div[@role='main']//span[contains(text(),'Удалить все письма со спамом')]")
                        clear_2.click()
                        time.sleep(2)
                        ActionChains(driver).key_down(Keys.ENTER).perform()
                        time.sleep(2)
                        break
                    except NoSuchElementException:
                        pass
                        break
                
                all_mail = driver.find_element(By.XPATH,"//div[@data-tooltip='Вся почта']//a[contains(text(),'Вся почта')]")
                driver.execute_script("arguments[0].click();", all_mail)
                time.sleep(2)
            
                cool = self.check_exists_by_xpath("//tr[@class='TD']//td[contains(text(),'Писем нет. Нашим серверам не хватает внимания.')]")

                if cool is True:
                    try:
                        # write script
                        script = "alert('There is no spam here anymore! Success!')"
                        # generate a alert via javascript
                        driver.execute_script(script)
                        time.sleep(3)
                        ActionChains(driver).key_down(Keys.ENTER).perform()
                    except UnexpectedAlertPresentException as e:
                        pass
                    print("")
                    print("There is no spam here anymore! Success!") 
                    break
                else:
                    try:
                        # write script
                        script = "alert('There is still something else to delete here! Failure!')"
                        # generate a alert via javascript
                        driver.execute_script(script)
                        time.sleep(3)
                        ActionChains(driver).key_down(Keys.ENTER).perform()
                    except UnexpectedAlertPresentException as e:
                        pass
                    print("")
                    print("There is still something else to delete here! Failure!")
                    continue
                
            ################################################################################################################################################################################
            except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException, JavascriptException, TimeoutException) as ex:
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
                print("Error! The requested HTML-element was not found on the HTML-page!")
                print("")
                self.PrintException()
                print("")
                ex_type, ex_value, ex_traceback = sys.exc_info()
                print("Exception type: %s" %ex_type.__name__)
                print("")
                print(f"Exception message: {ex.msg}")
                print("----------------------------------------------------------------------") 
                print("TEST FAILED (requested element was not found on page)")
                # exit_1 = True 
                self.tearDown()
                os._exit(0)
                
                # to see how test falls
                # sys.exit()
            ################################################################################################################################################################################
            # FUNCTION END
            
        # exit-exit
        # if exit_1 == True:
        #     os._exit(0)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except (NoSuchElementException, TimeoutException) as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except (NoSuchElementException, TimeoutException) as e: return False
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