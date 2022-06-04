# -*- coding: utf-8 -*-
from asyncio import log
import linecache
import sys
import os
import traceback
from time import sleep
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
from selenium.common.exceptions import JavascriptException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import ElementClickInterceptedException

# if you authorized somewhere, then launch browser with your user session (just close your Chrome)
# options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data')

# how to deploy screen (all variants)
# options.add_argument("--start-maximized") # другой вариант как можно выполнить это (через опции)
# driver.set_window_size(1366, 768) # другой вариант как можно выполнить это (указав размер окна)

# hidden browser mode (suitable!!!)
# options.add_argument('--headless') 
# options.add_argument('--disable-gpu')

# t = time.time()
# driver.set_page_load_timeout(10)

# use for cmd:
# cd C:\Users\User\Desktop\2\experiments
# good_test.py > ./my_good_test_results.txt

# use for bat:
# echo.
# echo..START good_test.py
# CMD /c > ./my_good_test_results.txt "C:\Users\User\Desktop\2\my_experiments\good_test.py"

s = Service('C:\\chromedriver\\chromedriver.exe')
options = webdriver.ChromeOptions()

# product name
product = str("Трансмиссионное масло NISSAN CVT NS-2, 5л")

# verifiable counter (in this test always must quantity counter = 1)
counter = str("//a[@href='/cart']//span[contains(@class,'tsCaptionBold') and contains(text(),'1')]")

# removing extra traceback
sys.tracebacklimit = 0

# use Colorama to make Termcolor work on Windows too
init(autoreset = True)

class ProductStore(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=s, options=options)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
        # неявное ожидание (когда страница ещё только загружается и элемента на ней может ещё не быть)
        self.driver.implicitly_wait(3)
        
        # явное ожидание (когда нужно дождаться выполнения неких условий прежде чем идти дальше)
        self.wait = WebDriverWait(self.driver, 3) 
        
    # method (function) for highlighting elements
    def highlight(self, element):
        # highlights (it blinks) selenium webdriver element
        # if element was not highlighted before click, it means
        # it will not find it, my special alert will confirm same
        self.driver = element._parent
        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
        original_style = element.get_attribute('style')
        apply_style("background: yellow; border: 4px solid red;")
        time.sleep(2)
        apply_style(original_style)
        
    # method (function) for printing filename, linenumber,
    # line itself and exception descrpition (if exception)
    def PrintException(self):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        # print("")
        print('EXCEPTION IN: =>\nPATH / FILE: {} =>\nLINE NUMBER: {} =>\nVARIABLE / ELEMENT: {}'.format(filename, lineno, line.strip()))
        
    # method (function) used for checking is there element on page
    def check_exists_by_xpath(self, xpath):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except (NoSuchElementException, TimeoutException) as e: return False
        return True
       
    # method (function) for creating ordering
    def creating_order(self):
        try: 
            # driver-driver    
            driver = self.driver

            # necessary URL
            driver.get("https://www.ozon.ru/")

            # how to deploy screen
            driver.maximize_window()
            time.sleep(2)

            # enter select product category mode (open modal window)
            select = driver.find_element(By.XPATH,"//span[@title='Везде']")
            driver.execute_script("arguments[0].scrollIntoView();", select)
            self.highlight(select)
            select.click()
            time.sleep(2)

            # going down up to highlighted categories
            discount = driver.find_element(By.XPATH,"//div[contains(text(),'Уценённые товары')]")
            driver.execute_script("arguments[0].scrollIntoView();", discount)
            self.highlight(discount)
            time.sleep(2)

            # select specific category
            category = driver.find_element(By.XPATH,"//div[contains(text(),'Автотовары')]")
            driver.execute_script("arguments[0].scrollIntoView();", category)
            self.highlight(category)
            category.click()
            time.sleep(2)

            # text-box + variable
            text_box = driver.find_element(By.NAME,"text")
            text_box.click()
            self.highlight(text_box)
            text_box.send_keys(product)
            time.sleep(2)

            # highlighting - [search] + [enter]
            search = driver.find_element(By.XPATH,"//div[@id='stickyHeader']//form[@action='/search']//button")
            driver.execute_script("arguments[0].scrollIntoView();", search)
            self.highlight(search)
            ActionChains(driver).key_down(Keys.ENTER).perform()
            time.sleep(2)

            # down + down + down
            actions = ActionChains(driver) 
            actions.send_keys(Keys.ARROW_DOWN * 8)
            actions.perform()
            time.sleep(2)

            # select necessary check-box
            check_box = driver.find_element(By.XPATH,"//div[@class='ui-ba5']//span[contains(text(),'NISSAN')]")
            self.highlight(check_box)
            time.sleep(2)
            driver.execute_script("arguments[0].click();", check_box)
            time.sleep(2)

            # down + down + down
            actions = ActionChains(driver) 
            actions.send_keys(Keys.ARROW_DOWN * 8)
            actions.perform()
            time.sleep(2)

            # select necessary toggle-switch (two elements are specially selected)
            toggle = driver.find_element(By.XPATH,"//div[@value='Товары со скидкой']")
            self.highlight(toggle)
            time.sleep(2)
            driver.find_element(By.XPATH,"//div[@value='Товары со скидкой']//div[@class='ui-ba6']").click()
            time.sleep(2)

            # down + down + down
            actions = ActionChains(driver) 
            actions.send_keys(Keys.ARROW_DOWN * 8)
            actions.perform()
            time.sleep(2)

            # select another one necessary toggle-switch (here needed two elements)
            toggle_1 = driver.find_element(By.XPATH,"//div[@value='Высокий рейтинг']")
            self.highlight(toggle_1)
            time.sleep(2)
            driver.find_element(By.XPATH,"//div[@value='Высокий рейтинг']//div[@class='ui-ba6']").click()
            time.sleep(2)

            # down + down + down
            downs = ActionChains(driver) 
            downs.send_keys(Keys.ARROW_DOWN * 12)
            downs.perform()
            time.sleep(2)

            # add to product basket
            add = driver.find_element(By.XPATH,"//*[contains(text(),'В корзину')]")
            self.highlight(add)
            driver.execute_script("arguments[0].click();", add)
            time.sleep(2)
        ###############################################################################################################################################
        except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, JavascriptException, TimeoutException) as ex:
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
            print("----------------------------------------------------------------------")
            self.tearDown()
            # driver.quit()
            # sys.exit()
            os._exit(0) # comment in PyCharm / or comment to see how test falls
        ###############################################################################################################################################
        # FUNCTION END (method for creating ordering)
    
    # test method of checking that
    # counter is being deleted
    def test_check(self):
            
        # FUNCTION STARTING (method for creating ordering)
        self.creating_order() # first starting
        
        ###############################################################################################################################################
        # ALL MAIN CHECKS START    
        try:  
            # driver again    
            driver = self.driver
            
            # quantity highlighting (1)
            quantity = driver.find_element(by=By.XPATH, value=counter)
            self.highlight(quantity)
            time.sleep(2)

            # checking that product is in basket by necessary quantity
            # 1 - first check (checking quantity)
            if quantity.text == "1":
                print("----------------------------------------------------------------------")
                print("")
                print(Fore.GREEN + "1 - first check  = done! (necessary quantity product is in basket)")
            else:
                print("")
                print(Fore.RED + "1 - first check  = error! (quantity does not match stated)")

            # button minus - [-] (remove product)
            minus = driver.find_element(By.XPATH,"//div[@data-widget='megaPaginator']//div[@data-widget='searchResultsV2']//button[@type='button']")
            self.highlight(minus)
            minus.click()
            time.sleep(2)

            # 2 - second check (that, counter was removed)
            while 1==1:
        
                counter_1 = self.check_exists_by_xpath(counter)

                if counter_1 is False:
                    try:
                        # write script
                        script = """alert(`После нажатия кнопки - [ - ] счётчик для количества товара пропал.
Всё правильно, так и должно быть и этот тест был упешно пройден.
Счётчик для количества товара на странице найден не был. Success!`)"""
                        # generate a alert via javascript
                        driver.execute_script(script)
                        time.sleep(8)
                        ActionChains(driver).key_down(Keys.ENTER).perform()
                    except UnexpectedAlertPresentException as e:
                        pass
                    print("")
                    print(Fore.GREEN + "2 - second check = done! (counter was removed)")
                    break
                else:
                    try:
                        qty_1 = driver.find_element(by=By.XPATH, value=counter)
                        self.highlight(qty_1)
                        # write script
                        script = """alert(`После нажатия btn - [ - ] счётчик количества товара не пропал.
Error! Error! Такого не должно быть, данный тест не был пройден.
Счётчик для количества товара на странице был найден. Failure!`)"""
                        # generate a alert via javascript
                        driver.execute_script(script)
                        time.sleep(80)
                        ActionChains(driver).key_down(Keys.ENTER).perform()
                    except UnexpectedAlertPresentException as e:
                        pass
                    print("")
                    print(Fore.RED + "2 - second check = error! (counter was not removed)")
                    break
                
            time.sleep(1)

            # add to product basket (2)
            add_1 = driver.find_element(By.XPATH,"//*[contains(text(),'В корзину')]")
            self.highlight(add_1)
            driver.execute_script("arguments[0].click();", add_1)
            time.sleep(2)

            # quantity highlighting (2)
            quantity_1 = driver.find_element(by=By.XPATH, value=counter)
            self.highlight(quantity_1)
            time.sleep(2)

            # 3 - third check (one more checking quantity) (2)
            if quantity_1.text == "1":
                print("")
                print(Fore.GREEN + "3 - third check  = done! (necessary quantity product is in basket)")
            else:
                print("")
                print(Fore.RED + "3 - third check  = error! (quantity does not match stated)")

            # button - [basket] + highlighting
            basket = driver.find_element(by=By.XPATH, value="//*[contains(text(),'Корзина')]")
            self.highlight(basket)
            basket.click()
            time.sleep(2)

            # remove modal window + highlighting product on page
            ActionChains(driver).key_down(Keys.ESCAPE).perform()
            time.sleep(2)

            # product highlighting 
            item = driver.find_element(by=By.XPATH, value=f"//*[contains(text(),'{product}')]")
            self.highlight(item)
            time.sleep(1)

            # button - [delete] (open modal window)
            delete = driver.find_element(By.XPATH,"//div[@data-widget='split']//button[@type='button']//span[text()='Удалить']")
            self.highlight(delete)
            delete.click()
            time.sleep(2)

            # button - [delete] (remove product and counter)
            delete_1 = driver.find_element(By.XPATH,"//div[@class='vue-portal-target']//button[@type='button']//span[text()='Удалить']")
            self.highlight(delete_1)
            delete_1.click()
            time.sleep(2)            

            # 4 - fourth check (that again, counter was removed)
            while 1==1:
        
                counter_2 = self.check_exists_by_xpath(counter)

                if counter_2 is False:
                    try:
                        # write script
                        script = """alert(`После нажатия btn - [delete] счётчик для количества товара пропал.
Всё правильно, так и должно быть и этот тест был упешно пройден.
Счётчик для количества товара на странице найден не был. Success!`)"""
                        # generate a alert via javascript
                        driver.execute_script(script)
                        time.sleep(8)
                        ActionChains(driver).key_down(Keys.ENTER).perform()
                    except UnexpectedAlertPresentException as e:
                        pass
                    print("")
                    print(Fore.GREEN + "4 - fourth check = done! (counter was removed again)")
                    break
                else:
                    try:
                        qty_2 = driver.find_element(by=By.XPATH, value=counter)
                        self.highlight(qty_2)
                        # write script
                        script = """alert(`После нажатия - [удалить] счётчик количества товара не пропал.
Error! Error! Такого не должно быть, данный тест не был пройден.
Счётчик для количества товара на странице был найден. Failure!`)"""
                        # generate a alert via javascript
                        driver.execute_script(script)
                        time.sleep(8)
                        ActionChains(driver).key_down(Keys.ENTER).perform()
                    except UnexpectedAlertPresentException as e:
                        pass
                    print("")
                    print(Fore.RED + "4 - fourth check = error! (counter was not removed)")
                    break
            
            time.sleep(1)

            # Now to do everything is everything again is again!!!
            ###############################################################################################################################################
            # FUNCTION STARTING (method for creating ordering)
            self.creating_order() # second starting

            # quantity highlighting (3)
            quantity_2 = driver.find_element(by=By.XPATH, value=counter)
            self.highlight(quantity_2)
            time.sleep(2)

            # checking that product is in basket by necessary quantity (3)
            # 5 - fifth check (checking quantity)
            if quantity_2.text == "1":
                print("")
                print(Fore.GREEN + "5 - fifth check  = done! (necessary quantity product is in basket)")
            else:
                print("")
                print(Fore.RED + "5 - fifth check  = error! (quantity does not match stated)")

            # button - [basket] + highlighting (2)
            basket_1 = driver.find_element(by=By.XPATH, value="//*[contains(text(),'Корзина')]")
            self.highlight(basket_1)
            basket_1.click()
            time.sleep(2)

            # remove modal window + highlighting product on page
            # ActionChains(driver).key_down(Keys.ESCAPE).perform()
            # time.sleep(2)

            # product highlighting (2)
            item_1 = driver.find_element(by=By.XPATH, value=f"//*[contains(text(),'{product}')]")
            self.highlight(item_1)
            time.sleep(1)

            # delete ALL!!! (open modal window)
            delete_ALL = driver.find_element(by=By.XPATH, value="//*[contains(text(),'Удалить выбранные')]")
            self.highlight(delete_ALL)
            delete_ALL.click()
            time.sleep(2)

            # button - [delete] (remove all products and counter) (2)
            delete_2 = driver.find_element(By.XPATH,"//div[@class='ui-i1']//span[text()='Удалить']")
            self.highlight(delete_2)
            delete_2.click()
            time.sleep(2)

            # 6 - sixth check (that again-again, counter was removed)
            while 1==1:
        
                counter_3 = self.check_exists_by_xpath(counter)

                if counter_3 is False:
                    try:
                        # write script
                        script = """alert(`После нажатия btn - [delete] счётчик для количества товара пропал.
Всё правильно, так и должно быть и этот тест был упешно пройден.
Счётчик для количества товара на странице найден не был. Success!`)"""
                        # generate a alert via javascript
                        driver.execute_script(script)
                        time.sleep(8)
                        ActionChains(driver).key_down(Keys.ENTER).perform()
                    except UnexpectedAlertPresentException as e:
                        pass
                    print("")
                    print(Fore.GREEN + "6 - sixth check  = done! (counter was removed again-again)")
                    print(Fore.RESET + "")
                    # print("----------------------------------------------------------------------") # for (.bat) file start 
                    break
                else:
                    quantity_3 = driver.find_element(by=By.XPATH, value=counter)
                    self.highlight(quantity_3)
                    try:
                        # write script
                        script = """alert(`После нажатия - [удалить] счётчик количества товара не пропал.
Error! Error! Такого не должно быть, данный тест не был пройден.
Счётчик для количества товара на странице был найден. Failure!`)"""
                        # generate a alert via javascript
                        driver.execute_script(script)
                        time.sleep(10)
                        ActionChains(driver).key_down(Keys.ENTER).perform()
                    except UnexpectedAlertPresentException as e:
                        pass
                    print("")
                    print(Fore.RED + "6 - sixth check  = error! (counter was not removed)")
                    print(Fore.RESET + "")
                    # print("----------------------------------------------------------------------") # for (.bat) file start
                    break
        ###############################################################################################################################################
        except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, JavascriptException, TimeoutException) as ex:
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
            # print(str(ex))

            # `Get current system exception
            ex_type, ex_value, ex_traceback = sys.exc_info()

            # `Extract unformatter stack traces as tuples
            # trace_back = traceback.extract_tb(ex_traceback)

            # `Format stacktrace
            # stack_trace = list()

            # for trace in trace_back:
            #     stack_trace.append("File: %s , Line: %d, Func.Name: %s, Message: %s" % (trace[0], trace[1], trace[2], trace[3]))

            self.PrintException()
            print("")
            print("Exception type: %s" %ex_type.__name__)
            print("")
            # print("Exception message: %s" %ex_value)
            print(f"Exception message: {ex.msg}")
            # log.logger.exception(f"Exception message: {ex.msg}", exc_info=False)
            # print("")
            # print("Stack trace: %s" %stack_trace)
            # print("----------------------------------------------------------------------") # for (.bat) file start
        ###############################################################################################################################################
            
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except (NoSuchElementException, TimeoutException) as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except (NoSuchElementException, TimeoutException) as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        # time.sleep(14) # for CMD

if __name__ == "__main__":
    unittest.main()