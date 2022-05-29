# -*- coding: utf-8 -*-
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

# use Colorama to make Termcolor work on Windows too
init (autoreset = True)

sys.tracebacklimit = 0
options = webdriver.ChromeOptions()
s = Service('C:\\chromedriver\\chromedriver.exe') 

# if you authorized somewhere, then launch browser with your user session (just close your Chrome)
# options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data')

# hidden browser mode (suitable!!!)
# options.add_argument('--headless') 
# options.add_argument("--no-sandbox")
# options.add_argument('--disable-gpu')
# options.add_argument("--disable-dev-shm-usage")

# use for cmd:
# cd C:\Users\User\Desktop\2\test-automation (Selenium+Python)\7
# test-test.py > ./my_test-test_results.txt

# use for bat:
# echo.
# echo..START test-test
# CMD /c > ./my_test-test_results.txt "C:\Users\User\Desktop\2\test-automation (Selenium+Python)\0\test-test.py"

class ProductStore(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=s, options=options)
        # неявное ожидание (когда страница ещё только загружается и элемента на ней может ещё не быть)
        self.driver.implicitly_wait(3) 
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_test(self):

        try: 

            # function used for checking is there element on page
            def check_exists_by_xpath(xpath):
                try:
                    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                except (NoSuchElementException, TimeoutException) as e: return False
                return True
                
            driver = self.driver
            # how to deploy screen (all variants)
            # options.add_argument("--start-maximized") # другой вариант как можно выполнить это (через опции)
            # driver.set_window_size(1366, 768) # другой вариант как можно выполнить это (указав размер окна)

            # function for highlighting elements
            def highlight(element):
                # highlights (it blinks) selenium webdriver element
                # if element was not highlighted before click, it means
                # it will not find it, my special alert will confirm same
                driver = element._parent
                def apply_style(s):
                    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
                original_style = element.get_attribute('style')
                apply_style("background: yellow; border: 2px solid red;")
                time.sleep(2)
                apply_style(original_style)

            # явное ожидание (когда нужно дождаться выполнения неких условий прежде чем идти дальше)
            wait = WebDriverWait(driver, 3)

            # t = time.time()
            # driver.set_page_load_timeout(10)

            # product name + URL
            product = str("NISSAN  NS-2 CVT Fluid, 5л")
            driver.get("https://www.ozon.ru/")

            # how to deploy screen
            driver.maximize_window()
            time.sleep(2)

            # enter select product category mode (open modal window)
            select = driver.find_element(By.XPATH,"//span[@title='Везде']")
            driver.execute_script("arguments[0].scrollIntoView();", select)
            highlight(select)
            select.click()
            time.sleep(2)

            # going down up to highlighted categories
            discount = driver.find_element(By.XPATH,"//div[contains(text(),'Уценённые товары')]")
            driver.execute_script("arguments[0].scrollIntoView();", discount)
            highlight(discount)
            time.sleep(2)

            # select specific category
            category = driver.find_element(By.XPATH,"//div[contains(text(),'Автотовары')]")
            driver.execute_script("arguments[0].scrollIntoView();", category)
            highlight(category)
            category.click()
            time.sleep(2)

            # text-box + variable
            text_box = driver.find_element(By.NAME,"text")
            text_box.click()
            highlight(text_box)
            text_box.send_keys(product)
            time.sleep(2)

            # highlighting - [search] + [enter]
            search = driver.find_element(By.CLASS_NAME,"wv8")
            driver.execute_script("arguments[0].scrollIntoView();", search)
            highlight(search)
            ActionChains(driver).key_down(Keys.ENTER).perform()
            time.sleep(2)

            # down + down + down
            actions = ActionChains(driver) 
            actions.send_keys(Keys.ARROW_DOWN * 8)
            actions.perform()
            time.sleep(2)

            # select necessary check-box
            check_box = driver.find_element(By.XPATH,"//div[@class='u7v']//span[contains(text(),'NISSAN')]")
            highlight(check_box)
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
            highlight(toggle)
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
            highlight(toggle_1)
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
            highlight(add)
            driver.execute_script("arguments[0].click();", add)
            time.sleep(2)

            # quantity highlighting (1)
            quantity = driver.find_element(by=By.XPATH, value="//span[@class='tsCaptionBold cl6']")
            highlight(quantity)
            time.sleep(2)

            # checking that product is in basket by necessary quantity
            # 1 - first check (checking quantity)
            if quantity.text == "1":
                print("")
                print("")
                print(Fore.GREEN + "1 - first check  = done! (necessary quantity product is in basket)")
            else:
                print("")
                print(Fore.RED + "1 - first check  = error! (quantity does not match stated)")

            # button minus - [-] (remove product)
            minus = driver.find_element(By.XPATH,"//div[@class='xc3']//button[@type='button']")
            highlight(minus)
            minus.click()
            time.sleep(2)

            # 2 - second check (that, counter was removed)
            while 1==1:
        
                counter = check_exists_by_xpath("//span[@class='tsCaptionBold cl6']")

                if counter is False:
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
                        qty_1 = driver.find_element(by=By.XPATH, value="//span[@class='tsCaptionBold cl6']")
                        highlight(qty_1)
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

            # add to product basket (2)
            add_1 = driver.find_element(By.XPATH,"//*[contains(text(),'В корзину')]")
            highlight(add_1)
            driver.execute_script("arguments[0].click();", add_1)
            time.sleep(2)

            # quantity highlighting (2)
            quantity_1 = driver.find_element(by=By.XPATH, value="//span[@class='tsCaptionBold cl6']")
            highlight(quantity_1)
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
            highlight(basket)
            basket.click()
            time.sleep(2)

            # remove modal window + highlighting product on page
            ActionChains(driver).key_down(Keys.ESCAPE).perform()
            time.sleep(2)

            # product highlighting 
            item = driver.find_element(by=By.XPATH, value=f"//*[contains(text(),'{product}')]")
            highlight(item)

            # button - [delete] (open modal window)
            delete = driver.find_element(By.XPATH,"//div[@class='na7']//span[text()='Удалить']")
            highlight(delete)
            delete.click()
            time.sleep(2)

            # button - [delete] (remove product and counter)
            delete1 = driver.find_element(By.XPATH,"//div[@class='na3 ui-c1']//span[text()='Удалить']")
            highlight(delete1)
            delete1.click()
            time.sleep(2)            

            # 4 - fourth check (that again, counter was removed)
            while 1==1:
        
                counter_1 = check_exists_by_xpath("//span[@class='tsCaptionBold cl6']")

                if counter_1 is False:
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
                        qty_2 = driver.find_element(by=By.XPATH, value="//span[@class='tsCaptionBold cl6']")
                        highlight(qty_2)
                        # write script
                        script = """alert(`После нажатия - [удалить] счётчик количества товара не пропал.
Error! Error! Такого не должно быть, данный тест не был пройден.
Счётчик для количества товара на странице был найден. Failure!`)"""
                        # generate a alert via javascript
                        driver.execute_script(script)
                        time.sleep(80)
                        ActionChains(driver).key_down(Keys.ENTER).perform()
                    except UnexpectedAlertPresentException as e:
                        pass
                    print("")
                    print(Fore.RED + "4 - fourth check = error! (counter was not removed)")
                    break

            # Now to do everything is everything again is again!!!
            ############################################################################################################################

            # enter select product category mode (open modal window) (2)
            select_1 = driver.find_element(By.XPATH,"//span[@title='Везде']")
            driver.execute_script("arguments[0].scrollIntoView();", select_1)
            highlight(select_1)
            select_1.click()
            time.sleep(2)

            # select_1 = driver.find_elements_by_xpath("//span[@title='Везде']")
            # WebDriverWait(driver, 4).until(EC.presence_of_all_elements_located((By.XPATH,"//span[@title='Везде']")))
            # select_1[0].click()

            # going down up to highlighted categories (2)
            discount_1 = driver.find_element(By.XPATH,"//div[contains(text(),'Уценённые товары')]")
            driver.execute_script("arguments[0].scrollIntoView();", discount_1)
            highlight(discount_1)
            time.sleep(2)

            # select specific category (2)
            category_1 = driver.find_element(By.XPATH,"//div[contains(text(),'Автотовары')]")
            driver.execute_script("arguments[0].scrollIntoView();", category_1)
            highlight(category_1)
            category_1.click()
            time.sleep(2)

            # text-box + variable (2)
            text_box_1 = driver.find_element(By.NAME,"text")
            text_box_1.click()
            highlight(text_box_1)
            text_box_1.send_keys(product)
            time.sleep(2)

            # highlighting - [search] + [enter] (2)
            search_1 = driver.find_element(By.CLASS_NAME,"wv8")
            driver.execute_script("arguments[0].scrollIntoView();", search_1)
            highlight(search_1)
            ActionChains(driver).key_down(Keys.ENTER).perform()
            time.sleep(2)

            # down + down + down
            actions = ActionChains(driver) 
            actions.send_keys(Keys.ARROW_DOWN * 8)
            actions.perform()
            time.sleep(2)

            # select necessary check-box (2)
            check_box_1 = driver.find_element(By.XPATH,"//div[@class='u7v']//span[contains(text(),'NISSAN')]")
            highlight(check_box_1)
            time.sleep(2)
            driver.execute_script("arguments[0].click();", check_box_1)
            time.sleep(2)

            # down + down + down
            actions = ActionChains(driver) 
            actions.send_keys(Keys.ARROW_DOWN * 8)
            actions.perform()
            time.sleep(2)
        
            # select necessary toggle-switch (two elements are specially selected) (2)
            toggle_1 = driver.find_element(By.XPATH,"//div[@value='Товары со скидкой']")
            highlight(toggle_1)
            time.sleep(2)
            driver.find_element(By.XPATH,"//div[@value='Товары со скидкой']//div[@class='ui-ba6']").click()
            time.sleep(2)

            # down + down + down
            actions = ActionChains(driver) 
            actions.send_keys(Keys.ARROW_DOWN * 8)
            actions.perform()
            time.sleep(2)

            # select another one necessary toggle-switch (here needed two elements) (2)
            toggle_1 = driver.find_element(By.XPATH,"//div[@value='Высокий рейтинг']")
            highlight(toggle_1)
            time.sleep(2)
            driver.find_element(By.XPATH,"//div[@value='Высокий рейтинг']//div[@class='ui-ba6']").click()
            time.sleep(2)

            # down + down + down
            downs = ActionChains(driver) 
            downs.send_keys(Keys.ARROW_DOWN * 12)
            downs.perform()
            time.sleep(2)

            # add to product basket (2)
            add_1 = driver.find_element(By.XPATH,"//*[contains(text(),'В корзину')]")
            highlight(add_1)
            driver.execute_script("arguments[0].click();", add_1)
            time.sleep(2)

            # quantity highlighting (3)
            quantity_2 = driver.find_element(by=By.XPATH, value="//span[@class='tsCaptionBold cl6']")
            highlight(quantity_2)
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
            highlight(basket_1)
            basket_1.click()
            time.sleep(2)

            # remove modal window + highlighting product on page
            # ActionChains(driver).key_down(Keys.ESCAPE).perform()
            # time.sleep(2)

            # product highlighting (2)
            item_1 = driver.find_element(by=By.XPATH, value=f"//*[contains(text(),'{product}')]")
            highlight(item_1)

            # delete ALL!!! (open modal window)
            delete_ALL = driver.find_element(by=By.XPATH, value="//*[contains(text(),'Удалить выбранные')]")
            highlight(delete_ALL)
            delete_ALL.click()
            time.sleep(2)

            # button - [delete] (remove all products and counter) (2)
            delete_2 = driver.find_element(By.XPATH,"//div[@class='na3 ui-c1']//span[text()='Удалить']")
            highlight(delete_2)
            delete_2.click()
            time.sleep(2)

            # 6 - sixth check (that again-again, counter was removed)
            while 1==1:
        
                counter_2 = check_exists_by_xpath("//span[@class='tsCaptionBold cl6']")

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
                    print(Fore.GREEN + "6 - sixth check  = done! (counter was removed again-again)")
                    break
                else:
                    quantity_3 = driver.find_element(by=By.XPATH, value="//span[@class='tsCaptionBold cl6']")
                    highlight(quantity_3)
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
                    break
        
            ############################################################################################################################

        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementClickInterceptedException, JavascriptException) as ex:
            try:
                # write script
                script = "alert('Error! The requested element was not found on the HTML-page!')"
                # generate a alert via javascript
                driver.execute_script(script)
                time.sleep(5)
                ActionChains(driver).key_down(Keys.ENTER).perform()
            except UnexpectedAlertPresentException as e:
                pass
            print("")
            print("Error! The requested element was not found on the HTML-page!")
            print("")
            # print(str(ex))

            # `Get current system exception
            ex_type, ex_value, ex_traceback = sys.exc_info()

            # `Extract unformatter stack traces as tuples
            # trace_back = traceback.extract_tb(ex_traceback)

            # `Format stacktrace
            # stack_trace = list()

            # for trace in trace_back:
            #     stack_trace.append("File: %s , Line: %d, Func.Name: %s, Message: %s" % (trace[0], trace[1], trace[2], trace[3]))

            print("Exception type: %s" %ex_type.__name__)
            print("")
            print("Exception message: %s" %ex_value)
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