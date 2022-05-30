# -*- coding: utf-8 -*-
from asyncio import log
import linecache
import sys
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

# use for cmd:
# cd C:\Users\User\Desktop\2\experiments
# 0-1.py > ./my_test_results_0-1.txt

# use for bat:
# echo.
# echo..START: 0-1.py
# CMD /c > ./my_test_results.txt "C:\Users\User\Desktop\2\my_experiments\0-1.py"

class ProductStore(unittest.TestCase):
    def setUp(self):
        s = Service('C:\\chromedriver\\chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=s, options=options)
        
        # неявное ожидание (когда страница ещё только загружается и элемента на ней может ещё не быть)
        self.driver.implicitly_wait(3) 
        
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        sys.tracebacklimit = 0
        
        # use Colorama to make Termcolor work on Windows too
        init (autoreset = True)
        
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
        apply_style("background: yellow; border: 2px solid red;")
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
        print("")
        print('EXCEPTION IN: =>\nPATH / FILE: {} =>\nLINE NUMBER: {} =>\nVARIABLE / ELEMENT: {}'.format(filename, lineno, line.strip()))
        
    # method (function) used for checking is there element on page
    def check_exists_by_xpath(self, xpath):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except (NoSuchElementException, TimeoutException) as e: return False
        return True
    
    def test_order(self):
        try:
            # driver-driver
            driver = self.driver
            
            # product name + URL
            product = str("NISSAN  NS-2 CVT Fluid, 5л")
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
            search = driver.find_element(By.CLASS_NAME,"x1w")
            driver.execute_script("arguments[0].scrollIntoView();", search)
            self.highlight(search)
            ActionChains(driver).key_down(Keys.ENTER).perform()
            time.sleep(2)

            # how to click button - [search]
            # другой вариант как можно выполнить это
            # driver.find_element(By.LINK_TEXT,"cvt").click() 
            # time.sleep(2)

            # down + down + down
            actions = ActionChains(driver) 
            actions.send_keys(Keys.ARROW_DOWN * 8)
            actions.perform()
            time.sleep(2)

            # select necessary check-box
            check_box = driver.find_element(By.XPATH,"//div[@class='z5u']//span[contains(text(),'NISSAN')]")
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

            # select necessary toggle-switch
            # другой вариант как можно выполнить это 
            # driver.get("https://www.ozon.ru/search/?from_global=true&isdiscount=t&text=Nissan+NS-3+CVT%2C+5л")
            
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
            
            # button add more - [+] (XPATH - very difficult and was found only with Katalon Recorder)
            plus = driver.find_element(by=By.XPATH, value="(.//*[normalize-space(text()) and normalize-space(.)='−50%'])[1]/following::*[name()='svg'][3]")
            self.highlight(plus)
            plus.click()
            time.sleep(2)
            
            # button add more - [+] (CSS SELECTOR - if you go another way, but then there will be no highlighting of the element)
            # plus = driver.find_element(by=By.CSS_SELECTOR, value="#layoutPage > div.gy4 > div.container.gy5 > div:nth-child(2) > div:nth-child(2) > div.xi1 > div > div > div > div.iv0.v0i > div.i1v > div.iu5.i6u > div > div > div:nth-child(3) > div > button > span > svg > path")
            # self.highlight(plus)
            # plus.click()
            # time.sleep(2)
            
            """ Далее идёт своего рода защита от несанкционированного попадания скрипта в пустую корзину, т. к.
            далее будет иметь место проверка на наличие в корзине определённого товара по его html-элементу, то
            возможен и такой вариант при котором, этот html-элемент всё же может присутствовать в корзине в виде
            ранее искомого пользователем товара (в нижней части страницы корзины, например как предложение или
            реклама и т. д.). Но если сейчас html-элемент значка количества товара в корзине найден не будет,
            то и дальше скрипт никуда более не пойдёт и поэтому поводу можно будет уже больше не переживать. """

            # quantity highlighting (1)
            quantity_1 = driver.find_element(by=By.XPATH, value="//span[@class='tsCaptionBold co0']")
            self.highlight(quantity_1)
            time.sleep(2)

            # checking that product is in basket by necessary quantity
            # 1 - first check (checking quantity)
            if quantity_1.text == "2":
                print("")
                print("")
                print(Fore.GREEN + "1 - first check  = done! (necessary quantity product is in basket)")
            else:
                print("")
                print(Fore.RED + "1 - first check  = error! (quantity does not match stated)")

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

            # 2 - second check (that there is order for product and this product is in basket)
            while 1==1:
        
                element = self.check_exists_by_xpath(f"//*[contains(text(),'{product}')]")

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
                    print(Fore.GREEN + "2 - second check = done! (order has been created and product is in basket)")
                    break
                else:
                    print("")
                    print(Fore.RED + "2 - second check = error! (order has not been created and product is not in basket)")
                    break

            # clicking on combo-box + highlighting + select
            combo_box = driver.find_element(By.NAME,"filter")
            self.highlight(combo_box)
            combo_box.click()
            time.sleep(2)
            # ActionChains(driver).key_down(Keys.ARROW_DOWN).perform() # alternative (2)
            # time.sleep(1)
            # ActionChains(driver).key_down(Keys.ARROW_DOWN).perform() # alternative (2)
            # time.sleep(1)
            ActionChains(driver).key_down(Keys.ARROW_DOWN).perform() # alternative (2)
            time.sleep(1)
            ActionChains(driver).key_down(Keys.ARROW_DOWN).perform() # alternative (2)
            time.sleep(1)
            ActionChains(driver).key_down(Keys.ARROW_DOWN).perform() # (1)
            time.sleep(1)
            ActionChains(driver).key_down(Keys.ARROW_UP).perform() # (1)
            time.sleep(1)
            ActionChains(driver).key_down(Keys.ENTER).perform() # (1)
            time.sleep(2)

            # quantity highlighting (2)
            quantity_2 = driver.find_element(by=By.XPATH, value="//span[@class='tsCaptionBold co0']")
            self.highlight(quantity_2)
            time.sleep(2)

            # checking that product was added in basket (or was remove from basket)
            # 3 - third check (changing quantity in fact)
            if quantity_2.text == "1":
                print("")
                print(Fore.GREEN + "3 - third check  = done! (product was remove from basket / same quantity)")
                print("")
                print("")
                print(Fore.RESET + "What values were used:")
                print(f"product = {product}") 
                print("it is expected that quantity-1 = 2 (first check)")
                print("it is expected that quantity-2 = 1 (third check)")
            elif quantity_2.text == "3":
                print("")
                print(Fore.GREEN + "3 - third check  = done! (product was added from in basket / alternative)")
                print("")
                print("")
                print(Fore.RESET + "What values were used:")
                print(f"product = {product}") 
                print("it is expected that quantity-1 = 2 (first check)")
                print("it is expected that quantity-2 = 3 (third check)")
            else:
                print("")
                print(Fore.RED + "3 - third check  = error! (quantity does not match stated)")
                print("")
                print("")
                print(Fore.RESET + "What values were used:")
                print(f"product = {product}")
                print("it is expected that quantity-1 = 2 (first check)")
                print(f"it is expected that quantity-2 = 1 or 3,\nbut quantity-2 = {quantity_2.text} and it error (third check)")

            # transition buying product
            execute = driver.find_element(by=By.XPATH, value="//*[contains(text(),'Перейти к оформлению')]")
            self.highlight(execute)
            execute.click()
            time.sleep(4)

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
            print("")
            print("Error! The requested HTML-element was not found on the HTML-page!")
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
        # time.sleep(14)

if __name__ == "__main__":
    unittest.main()