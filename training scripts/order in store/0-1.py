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
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import WebDriverException

# ChromiumService + ChromiumOptions
# service = Service('C:\\chromedriver\\chromedriver.exe')
options = webdriver.ChromeOptions()

# if you authorized somewhere, then launch browser with your user session (just close your Chrome)
options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data')

# product name (часто будет заканчиваться)
product = str("Масло трансмиссионное Nissan")

# seller name (часто будет меняться)
seller = str("официальный дилер NISSAN") 

# changing class (иногда)
changing_class = str("ui-ab5")

# verifiable counter (can have any number, but will be
# caught if 0, and if not 1 or 3, then it will be an error)
# counter = str("//span[@class='tsCaptionBold cq3']") # just in case
counter = str("//a[@href='/cart']//span[contains(@class,'tsCaptionBold')]")

# removing extra traceback
sys.tracebacklimit = 0

# use Colorama to make Termcolor work on Windows too
init(autoreset = True)

class ProductStore(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe", options=options) 
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
        # неявное ожидание (когда страница ещё только загружается и элемента на ней может ещё не быть)
        self.driver.implicitly_wait(5)
        
        # явное ожидание (когда нужно дождаться выполнения неких условий прежде чем идти дальше)
        self.wait = WebDriverWait(self.driver, 5, 0.3)
        
    # function for highlighting elements
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
    
    # function for creating ordering
    def test_order(self):
        while 1==1:
            try:
                # driver-driver
                driver = self.driver
                
                # necessary URL
                driver.get("https://www.ozon.ru/")
                
                # how to deploy screen
                driver.maximize_window()
                time.sleep(2)
                
                # сhecking the title of the home page
                self.assertEqual(driver.title,'OZON — интернет-магазин. Миллионы товаров по выгодным ценам')

                # enters select product category mode (opens modal window)
                select = driver.find_element(By.XPATH,"//form[@action='/search']//span[@title='Везде']")
                driver.execute_script("arguments[0].scrollIntoView();", select)
                self.highlight(select)
                select.click()
                time.sleep(2)

                # goes down up to highlighted categories
                discount = driver.find_element(By.XPATH,"//div[contains(text(),'Уценённые товары')]")
                driver.execute_script("arguments[0].scrollIntoView();", discount)
                self.highlight(discount)
                time.sleep(2)

                # selects specific category
                category = driver.find_element(By.XPATH,"//div[contains(text(),'Автотовары')]")
                driver.execute_script("arguments[0].scrollIntoView();", category)
                self.highlight(category)
                category.click()
                time.sleep(2)

                # text-box + variable (product)
                text_box = driver.find_element(By.NAME,"text")
                text_box.click()
                self.highlight(text_box)
                text_box.send_keys(product)
                time.sleep(2)

                # button highlighting - [search] + presses key - [enter]
                search = driver.find_element(By.XPATH,"//div[@id='stickyHeader']//form[@action='/search']//button")
                driver.execute_script("arguments[0].scrollIntoView();", search)
                self.highlight(search)
                ActionChains(driver).key_down(Keys.ENTER).perform()
                time.sleep(2)

                # down + down + down
                actions = ActionChains(driver) 
                actions.send_keys(Keys.ARROW_DOWN * 14)
                actions.perform()
                time.sleep(2)

                # selects necessary check-box №1
                check_box_1 = driver.find_element(By.XPATH,f"//div[@class='{changing_class}']//span[contains(text(),'NISSAN')]")                
                self.highlight(check_box_1)
                time.sleep(2)
                driver.execute_script("arguments[0].click();", check_box_1)
                while 1==1:
                    try:
                        was_is_checked_box_1 = driver.find_element(By.XPATH,f"//span[contains(text(),'NISSAN')]/ancestor::div[@class='{changing_class}']/parent::label/input")
                        self.assertTrue(was_is_checked_box_1.is_selected())
                        break
                    except StaleElementReferenceException:
                        pass
                        continue
                time.sleep(2)
                
                # setting product price (optional)
                while 1==1:
                    try:
                        input = driver.find_element(By.XPATH,"//div[@unit='[object Object]']//p[contains(text(),'до')]/preceding-sibling::input")
                        driver.execute_script("arguments[0].scrollIntoView();", input)
                        
                        # up + up + up
                        actions = ActionChains(driver) 
                        actions.send_keys(Keys.ARROW_UP * 12)
                        actions.perform()
                        time.sleep(2)
                        
                        input.click()
                        actions = ActionChains(driver) 
                        actions.send_keys(Keys.BACKSPACE * 5)
                        actions.perform()
                        
                        input.send_keys('2000')
                        input.click()
                        self.highlight(input)
                        ActionChains(driver).key_down(Keys.ENTER).perform()
                        time.sleep(2)
                        
                        new_value = driver.find_element(By.XPATH,"//div[@unit='[object Object]']//p[contains(text(),'до')]/preceding-sibling::input").get_attribute("value")
                        self.assertIn('2000', new_value)
                        break
                    # if missing input, then script goes on 
                    except NoSuchElementException:
                        pass
                        break

                # selects necessary check-box №2
                check_box_2 = driver.find_element(By.XPATH,f"//div[@class='{changing_class}']//span[contains(text(),'{seller}')]")
                driver.execute_script("arguments[0].scrollIntoView();", check_box_2)
                
                # up + up + up
                actions = ActionChains(driver) 
                actions.send_keys(Keys.ARROW_UP * 12)
                actions.perform()
                time.sleep(2)
                
                self.highlight(check_box_2)
                time.sleep(2)
                driver.execute_script("arguments[0].click();", check_box_2)
                while 1==1:
                    try:
                        was_is_checked_box_2 = driver.find_element(By.XPATH,f"//span[contains(text(),'{seller}')]/ancestor::div[@class='{changing_class}']/parent::label/input")
                        self.assertTrue(was_is_checked_box_2.is_selected())
                        break
                    except StaleElementReferenceException:
                        pass
                        continue
                time.sleep(2)
                
                # selects toggle-switch №1 / this is extra toggle-switch (selects his optional)
                while 1==1:
                    try:
                        toggle_1 = driver.find_element(By.XPATH,"//div[@value='Товары со скидкой']")
                        driver.execute_script("arguments[0].scrollIntoView();", toggle_1)
                        
                        # up + up + up
                        actions = ActionChains(driver) 
                        actions.send_keys(Keys.ARROW_UP * 12)
                        actions.perform()
                        time.sleep(2)
                        
                        self.highlight(toggle_1)
                        time.sleep(2)
                        driver.find_element(By.XPATH,f"//div[@value='Товары со скидкой']//div[@class='{changing_class}']").click()
                        time.sleep(2)
                        break
                        # if missing toggle-switch, then script goes on 
                    except NoSuchElementException:
                        pass
                        break
                
                # selects one more toggle-switch №2 / this is extra toggle-switch (selects his optional)
                while 1==1:
                    try:
                        toggle_2 = driver.find_element(By.XPATH,"//div[@value='Высокий рейтинг']")
                        driver.execute_script("arguments[0].scrollIntoView();", toggle_2)
                        
                        # up + up + up
                        actions = ActionChains(driver) 
                        actions.send_keys(Keys.ARROW_UP * 12)
                        actions.perform()
                        time.sleep(2)
                        
                        self.highlight(toggle_2)
                        time.sleep(2)
                        driver.find_element(By.XPATH,f"//div[@value='Высокий рейтинг']//div[@class='{changing_class}']").click()
                        time.sleep(2)
                        break
                    # if missing toggle-switch, then script goes on 
                    except NoSuchElementException:
                        pass
                        break
                    
                # down to this element:
                deliver = driver.find_element(By.XPATH,"//*[contains(text(),'доставит')]")
                driver.execute_script("arguments[0].scrollIntoView();", deliver)

                # # up + up + up
                actions = ActionChains(driver) 
                actions.send_keys(Keys.ARROW_UP * 14)
                actions.perform()
                time.sleep(2)
                
                # shows selected categories (these elements is optional to show)
                categories = [
                "//button[@type='button']//span[contains(text(),'Цена: от')]",         
                "//button[@type='button']//span[contains(text(),'Бренды: NISSAN')]",                
                "//button[@type='button']//span[contains(text(),'Высокий рейтинг')]",   
                "//button[@type='button']//span[contains(text(),'Товары со скидкой')]",  
                f"//button[@type='button']//span[contains(text(),'Продавец: {seller}')]"             
                ]            
                their_number = 5
                for i in range(their_number):
                    try:
                        elements = driver.find_element(By.XPATH, categories[i])
                        self.highlight(elements)
                    except NoSuchElementException:
                        pass
                ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
                time.sleep(1)

                # adds to product basket
                add = driver.find_element(By.XPATH,"//*[contains(text(),'В корзину')]")
                self.highlight(add)
                driver.execute_script("arguments[0].click();", add)
                time.sleep(2)
                
                # presses button add more - [+] (XPATH - very difficult)
                one_unit = False
                while 1==1:
                    try:
                        plus = driver.find_element(by=By.XPATH, value="//div[@data-widget='megaPaginator']//div[@data-widget='searchResultsV2']//button[@type='button']/span[@style='border-radius: 8px;']/following::*[name()='svg'][1]")
                        self.highlight(plus)
                        plus.click()
                        time.sleep(2)
                        break
                    # if button - [+] cannot be pressed, then script goes on
                    except ElementClickInterceptedException:
                        pass
                        one_unit = True
                        break
                
                """ Далее идёт своего рода защита от несанкционированного попадания скрипта в пустую корзину, т. к.
                далее будет иметь место проверка на наличие в корзине определённого товара по его html-элементу, то
                возможен и такой вариант при котором, этот html-элемент всё же может присутствовать в корзине в виде
                ранее искомого пользователем товара (в нижней части страницы корзины, например как предложение или
                реклама и т. д.). Но если сейчас html-элемент значка количества товара в корзине найден не будет,
                то и дальше скрипт никуда более не пойдёт и поэтому поводу можно будет уже больше не переживать. """

                # сhecking what quantity is not zero + highlighting if qty > 0 (1)
                quantity_1 = driver.find_element(by=By.XPATH, value=counter)
                if quantity_1.text == "0":
                    print("----------------------------------------------------------------------")
                    print(f"Undetected element it is verifiable counter\nand obviously that quantity counter = {quantity_1.text}")
                    print(f"counter = '{counter}'")
                    raise NoSuchElementException
                else:
                    pass
                    self.highlight(quantity_1)
                    time.sleep(2)

                # checking that product is in basket by necessary quantity
                # 1 - first check (checking quantity)
                if quantity_1.text == "2":
                    print("\n----------------------------------------------------------------------")
                    print("")
                    print(Fore.GREEN + "1 - first check  = done!  (necessary quantity product is in basket)")
                    result_1 = True
                else:
                    print("\n----------------------------------------------------------------------")
                    print("")
                    print(Fore.RED + "1 - first check  = error! (quantity does not match stated)")
                    result_1 = False

                # presses button - [basket] + highlighting
                basket = driver.find_element(by=By.XPATH, value="//*[contains(text(),'Корзина')]")
                self.highlight(basket)
                basket.click()
                time.sleep(2)

                # removes extra modal window (if advertisement)
                ActionChains(driver).key_down(Keys.ESCAPE).perform()
                time.sleep(2)

                # product highlighting on page (because everyone products has seller)
                item = driver.find_element(by=By.XPATH, value=f"//*[contains(text(),'{seller}')]")
                self.highlight(item)

                # 2 - second check (that there is order for product and this product is in basket)
                while 1==1:
            
                    element = self.check_exists_by_xpath(f"//*[contains(text(),'{seller}')]")

                    if element is True:
                        try:
                            # write script
                            script = """alert(`Если видно это сообщение, то выбранный скриптом
товар находится в продуктовой корзине и кнопка - [Корзина]
была нажата. Заказ был создан и находится сейчас в статусе: «Ожидает оплаты».`)"""
                            # generate a alert via javascript
                            driver.execute_script(script)
                            time.sleep(8)
                            ActionChains(driver).key_down(Keys.ENTER).perform()
                        except UnexpectedAlertPresentException as e:
                            pass
                        print("")
                        print(Fore.GREEN + "2 - second check = done!  (order has been created and product is in basket)")
                        result_2 = True
                        break
                    else:
                        print("")
                        print(Fore.RED + "2 - second check = error! (order has not been created and product is not in basket)")
                        result_2 = False
                        break
                    
                time.sleep(1)

                # goes clicking on combo-box + highlighting + select
                combo_box = driver.find_element(By.NAME,"filter")
                self.highlight(combo_box)
                combo_box.click()
                time.sleep(2)
                
                # alternative choice is on 3 (quantity_2 = 3) / adds more products 
                ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
                time.sleep(1)
                ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
                time.sleep(1)
                ActionChains(driver).key_down(Keys.ENTER).perform()
                time.sleep(2)
                
                # if choice is on 1 (quantity_2 = 1) / removes excess products
                # ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
                # time.sleep(1)
                # ActionChains(driver).key_down(Keys.ARROW_UP).perform()
                # time.sleep(1)
                # ActionChains(driver).key_down(Keys.ENTER).perform()
                # time.sleep(2)

                # quantity highlighting
                quantity_2 = driver.find_element(by=By.XPATH, value=counter)
                self.highlight(quantity_2)
                time.sleep(2)
                
                # test results (will be selected by script)
                test_result_1 = str("TEST SUCCESSFULLY (all checks were successful)")
                test_result_2 = str("TEST partly SUCCESSFULLY (some of checks were not passed)")

                # checking that product was added in basket (or was remove from basket)
                # 3 - third check (changing quantity in fact)
                if quantity_2.text == "1":
                    print("")
                    print(Fore.GREEN + "3 - third check  = done!  (product was remove from basket / same quantity)")
                    print(Fore.RESET + "----------------------------------------------------------------------")
                    print("")
                    print(Fore.RESET + "What values were used:")
                    print(f"product = {product}") 
                    print("it is expected that quantity-1 = 2 (first check)")
                    print("it is expected that quantity-2 = 1 (third check)")
                    # for (.bat) file start
                    print("----------------------------------------------------------------------")
                    if result_1 == True and result_2 == True:
                        print(test_result_1)
                    elif result_1 == False or result_2 == False:
                        print(test_result_2)
                elif quantity_2.text == "3":
                    print("")
                    print(Fore.GREEN + "3 - third check  = done!  (product was added from in basket / alternative)")
                    print(Fore.RESET + "----------------------------------------------------------------------")
                    print("")
                    print(Fore.RESET + "What values were used:")
                    print(f"product = {product}") 
                    print("it is expected that quantity-1 = 2 (first check)")
                    print("it is expected that quantity-2 = 3 (third check)")
                    # for (.bat) file start
                    print("----------------------------------------------------------------------")
                    if result_1 == True and result_2 == True:
                        print(test_result_1)
                    elif result_1 == False or result_2 == False:
                        print(test_result_2) 
                else:
                    print("")
                    print(Fore.RED + "3 - third check  = error! (quantity does not match stated)")
                    print(Fore.RESET + "----------------------------------------------------------------------")
                    print("")
                    print("What values were used:")
                    print(f"product = {product}")
                    print("it is expected that quantity-1 = 2 (first check)")
                    print(f"it is expected that quantity-2 = 1 or 3,\nbut quantity-2 = {quantity_2.text} and it error (third check)")
                    # for (.bat) file start
                    print("----------------------------------------------------------------------") 
                    print(test_result_2) 

                # transition buying product
                execute = driver.find_element(by=By.XPATH, value="//*[contains(text(),'Перейти к оформлению')]")
                self.highlight(execute)
                execute.click()
                time.sleep(4)
                
                # warning (product quantity = 1)
                if one_unit != False:
                    print("")
                    print("")
                    print("")
                    print("======================= Attention! Attention! =======================")
                    print("The quantity of the required product on the website is only one unit!")
                    print("(required product quantity = 1 and 1 - first check cannot be passed)")
                    print("=====================================================================")
                    
                self.checking_basket()
                break
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
                
                # for (.bat) file start / or alternative
                print("----------------------------------------------------------------------") 
                print("TEST FAILED (requested element was not found on page)") 
                # break
                self.tearDown()
                os._exit(0)
                
                # to see how test falls
                # sys.exit()
            ################################################################################################################################################################################
            except WebDriverException:
                pass
                continue 
    
    # function for checking basket        
    def checking_basket(self):
        repeat = 5
        for i in range(repeat):
            try:
                # driver-driver
                driver = self.driver
            
                # goes to the basket
                driver.get('https://www.ozon.ru/cart')
                
                # сhecking the title of the basket
                self.assertEqual(driver.title,'OZON.ru - Моя корзина')
                
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
                delete_2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, del_2)))
                driver.execute_script("arguments[0].click();", delete_2)
                time.sleep(1)
                
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