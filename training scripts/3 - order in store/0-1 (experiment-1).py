# -*- coding: utf-8 -*-
from asyncio import log
import linecache
import textwrap
import datetime
import random
import sys
import re
import os
import traceback
import urllib.parse
from PIL import Image
from io import BytesIO
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

# for PowerShell:
# python -u "c:\Users\User\Desktop\2\my_experiments\0-1.py"

# for unittest:
# cd c:\Users\User\Desktop\2\my_experiments
# python -m unittest -v "0-1.py"

# ChromiumService + ChromiumOptions
# service = Service('C:\\chromedriver\\chromedriver.exe')
options = webdriver.ChromeOptions()

# if you authorized somewhere, then launch browser with your user session (just close your Chrome)
options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data')

# removes unnecessary system logs and warnings
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# product name (часто будет заканчиваться)
product = str("Трансмиссионное масло Nissan")

# product brand (смена редко)
brand = str("Nissan Marine")

# seller's name (часто будет меняться)
seller = str('ваши автозапчасти') 

# product price (часто будет меняться) 
price = str('1085')

# changing class (иногда бывает нужен)
changing_class = str("_6-a0")

# random number (1 / 2)
random_number = int(random.randint(1, 2))

# Initial quantity for pics index
pics_index = 1

# verifiable counter (can have any number, but will be
# caught if 0, and if not 1 or 3, then it will be an error)
# counter = str("//span[@class='tsCaptionBold cq3']") # just in case
counter = str("//a[@href='/cart']//span[contains(@class,'tsCaptionBold')]")

# removing extra traceback
sys.tracebacklimit = 0

# automatic color reset after color text output
init(autoreset = True)

class ProductStore(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe", options=options)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
        # неявное ожидание (когда страница ещё только загружается и элемента на ней может ещё не быть)
        self.driver.implicitly_wait(1.5)
        
        # явное ожидание (когда нужно дождаться выполнения неких условий прежде чем идти дальше)
        self.wait = WebDriverWait(self.driver, 1.5, 0.3)
        
    # function for highlighting elements
    def highlight(self, element):
        # highlights (it illuminates) html-element prior to pressed,
        # if this element was not highlighted before click, it means,
        # that his won't find, and my special alert will confirm same.
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
        print('\nEXCEPTION IN:\n \nPATH / FILE:\n{}\n \nLINE NUMBER: {}\n \nVARIABLE / ELEMENT:\n{}'.format(filename, lineno, line.strip()))
        
    # function used for checking is there element on page
    def check_exists_by_xpath(self, xpath):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except (NoSuchElementException, TimeoutException) as e: return False
        return True
    
    # function for getting the current time
    def extract_current_time(self):
        global current_time
        time_now = datetime.datetime.now()
        current_time = str(time_now).replace(" ", "")
        current_time = str(re.sub('[.:-]', '', current_time))
        
        start = 8 # how much to cut 
        stop = 20 # how much to pull
        slice_str = slice(start, stop)
        current_time = current_time[slice_str]
        current_time = int(current_time)
        return current_time
    
    # function for creating a screenshot
    def makes_screenshot(self):
        # n = str(random.randint(1, 10))
        global pics_index
        if pics_index < 7 and current_time > past_time:
            pics_index = pics_index + 1
        
        png = self.driver.get_screenshot_as_png() 
        im = Image.open(BytesIO(png))  
        im.save(f"C:\\Users\\User\\Desktop\\2\\my_experiments\\screenshots\\screenshot_{pics_index}.png")
        return pics_index
    
    # function for selects toggle-switch №1 / this is extra toggle-switch (this is optional) [# SWITH-1]
    def toggle_switch_1(self):
        while 1==1:
            try:
                toggle_1 = self.driver.find_element(By.XPATH,"//div[@value='Товары со скидкой']")
                actions = ActionChains(self.driver)
                actions.move_to_element(toggle_1).key_down(Keys.ARROW_DOWN).perform()
                ActionChains(self.driver).key_down(Keys.ARROW_DOWN).perform()
                
                self.highlight(toggle_1)
                self.driver.find_element(By.XPATH,f"//div[@value='Товары со скидкой']/label/input[@type='checkbox']/parent::label//span[contains(text(),'Товары со скидкой')]").click()
                time.sleep(1)
                break
                # if missing toggle-switch, then script goes on 
            except (NoSuchElementException, TimeoutException):
                pass
                break
    
    # function for selects one more toggle-switch №2 / this is extra toggle-switch (this is optional) [# SWITH-2]        
    def toggle_switch_2(self):
        while 1==1:
            try:
                toggle_2 = self.driver.find_element(By.XPATH,"//div[@value='Высокий рейтинг']")
                actions = ActionChains(self.driver)
                actions.move_to_element(toggle_2).key_down(Keys.ARROW_DOWN).perform()
                ActionChains(self.driver).key_down(Keys.ARROW_DOWN).perform()
                
                self.highlight(toggle_2)
                self.driver.find_element(By.XPATH,f"//div[@value='Высокий рейтинг']/label/input[@type='checkbox']/parent::label//span[contains(text(),'Высокий рейтинг')]").click()
                time.sleep(1)
                break
            # if missing toggle-switch, then script goes on
            except (NoSuchElementException, TimeoutException):
                pass
                break
            
    # function for setting product price (this is optional) [# SETTING the PRICE]       
    def product_price_3(self):
        while 1==1:
            try:
                # shows where the price setting takes place
                show_price = self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Цена')]")))
                show = self.driver.find_element_by_xpath("//div[contains(text(),'Цена')]")
                location = show.location
                X = int(location['x'])
                Y = int(location['y'])
                self.driver.execute_script(f"arguments[0].scrollTo({X}, {Y}); arguments[0].click();", show)
                ActionChains(self.driver).send_keys(Keys.ARROW_UP * 7).perform()
                self.highlight(show_price)
                
                input = self.driver.find_element(By.XPATH,"//div[@unit='[object Object]']//p[contains(text(),'до')]/preceding-sibling::input")
                actions = ActionChains(self.driver)
                actions.move_to_element(input).key_down(Keys.ARROW_DOWN).perform()
                self.highlight(input)
                input.click()
                actions.send_keys(Keys.BACKSPACE * 6).send_keys(price).key_down(Keys.ENTER).perform()
                time.sleep(2)
                break
            # if missing input / show_price, then script goes on 
            except (NoSuchElementException, TimeoutException):
                pass
                break
    
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
                
                # makes a screenshot for the report (pic №1) [loading web-page]
                global past_time, step_forward
                past_time = self.extract_current_time()
                step_forward = self.makes_screenshot()
                self.extract_current_time()
                self.makes_screenshot()
                
                # сhecking the title of the home page
                self.assertEqual(driver.title,'OZON — интернет-магазин. Миллионы товаров по выгодным ценам')
                ActionChains(driver).key_down(Keys.SPACE).perform()
                
                # declaring global variables 
                # (basket_is_empty and product)
                global basket_is_empty
                basket_is_empty = True
                global product
                
                # if basket is not empty then deletes everything
                quantity_0 = driver.find_element(by=By.XPATH, value=counter) 
                if quantity_0.text != "0":
                    basket_is_empty = False
                    print(f"basket_is_empty = {basket_is_empty}")
                    self.checking_basket()
                    driver.get("https://www.ozon.ru/")
                    self.assertEqual(driver.title,'OZON — интернет-магазин. Миллионы товаров по выгодным ценам')
                    ActionChains(driver).key_down(Keys.SPACE).perform()
                    
                # enters select product category mode (opens modal window)
                select = driver.find_element(By.XPATH,"//form[@action='/search']//span[@title='Везде']")
                driver.execute_script("arguments[0].scrollIntoView(true);", select)
                self.highlight(select)
                select.click()
                time.sleep(2)

                # goes down up to highlighted categories
                auto = driver.find_element(By.XPATH,"//div[contains(text(),'Автомобили')]")
                driver.execute_script("arguments[0].scrollIntoView(true);", auto)
                self.highlight(auto)
                time.sleep(2)

                # selects specific category
                category = driver.find_element(By.XPATH,"//div[contains(text(),'Автотовары')]")
                driver.execute_script("arguments[0].scrollIntoView(true);", category)
                self.highlight(category)
                category.click()
                time.sleep(2)

                # text-box (search-box) + variable value (product name)
                text_box = driver.find_element(By.NAME,"text")
                text_box.click()
                self.highlight(text_box)
                text_box.send_keys(product)
                time.sleep(2)
                entered_value = driver.find_element(By.NAME,"text").get_attribute("value")
                self.assertIn(product, entered_value)

                # button highlighting - [search] + presses key - [enter]
                search = driver.find_element(By.XPATH,"//div[@id='stickyHeader']//form[@action='/search']//button")
                driver.execute_script("arguments[0].scrollIntoView(true);", search)
                self.highlight(search)
                ActionChains(driver).key_down(Keys.ENTER).perform()
                time.sleep(2)
                
                # makes a screenshot for the report (pic №2) [value was entered]
                past_time = self.extract_current_time()
                step_forward = self.makes_screenshot()
                self.extract_current_time()
                self.makes_screenshot()
                
                # down + down + down
                # actions = ActionChains(driver) 
                # actions.send_keys(Keys.ARROW_DOWN * 18)
                # actions.perform()
                # time.sleep(2)
                
                # selects toggle-switch №1 / this is extra toggle-switch (this is optional) [# TOGGLE-SWITCH-1]
                switch_1 = self.check_exists_by_xpath("//div[@value='Товары со скидкой']")
                if switch_1 is True:
                    self.toggle_switch_1()
                    #
                elif switch_1 is False:
                    #
                    while 1==1:
                        try:
                            all_filters = driver.find_element(By.XPATH,"//span[contains(text(),'Все фильтры')]")
                            # driver.execute_script("arguments[0].scrollIntoView(true);", all_filters)
                            # actions = ActionChains(driver) 
                            # actions.send_keys(Keys.ARROW_UP * 12)
                            # actions.perform()
                            # time.sleep(1)
                            #
                            actions = ActionChains(driver)
                            actions.move_to_element(all_filters).key_down(Keys.ARROW_DOWN).perform()
                            time.sleep(2)
                            self.highlight(all_filters)
                            driver.execute_script("arguments[0].click(true);", all_filters)
                            time.sleep(2)
                            #
                            discounted_products = driver.find_element(by=By.XPATH, value="//div/span[contains(text(),'Товары со скидкой')]")
                            self.highlight(discounted_products)
                            webdriver.ActionChains(driver).click(discounted_products).perform()
                            time.sleep(2)
                            apply = driver.find_element(by=By.XPATH, value="//div/button/span/span[contains(text(),'Применить')]")
                            self.highlight(apply)
                            webdriver.ActionChains(driver).click(apply).perform()
                            time.sleep(2)
                            break
                            # if missing UI-elements, then script goes on 
                        except (NoSuchElementException, TimeoutException):
                            pass
                            break
                
                # selects one more toggle-switch №2 / this is extra toggle-switch (this is optional) [# TOGGLE-SWITCH-2]
                switch_2 = self.check_exists_by_xpath("//div[@value='Высокий рейтинг']")
                if switch_2 is True:
                    self.toggle_switch_2()
                    #
                elif switch_2 is False:
                    #
                    while 1==1:
                        try:
                            all_filters = driver.find_element(By.XPATH,"//span[contains(text(),'Все фильтры')]")
                            # driver.execute_script("arguments[0].scrollIntoView(true);", all_filters)
                            # actions = ActionChains(driver) 
                            # actions.send_keys(Keys.ARROW_UP * 12)
                            # actions.perform()
                            # time.sleep(1)
                            #
                            actions = ActionChains(driver)
                            actions.move_to_element(all_filters).key_down(Keys.ARROW_DOWN).perform()
                            time.sleep(2)
                            self.highlight(all_filters)
                            driver.execute_script("arguments[0].click(true);", all_filters)
                            time.sleep(2)
                            #
                            discounted_products = driver.find_element(by=By.XPATH, value="//div/span[contains(text(),'Высокий рейтинг')]")
                            self.highlight(discounted_products)
                            webdriver.ActionChains(driver).click(discounted_products).perform()
                            time.sleep(2)
                            apply = driver.find_element(by=By.XPATH, value="//div/button/span/span[contains(text(),'Применить')]")
                            self.highlight(apply)
                            webdriver.ActionChains(driver).click(apply).perform()
                            time.sleep(2)
                            break
                            # if missing UI-elements, then script goes on 
                        except (NoSuchElementException, TimeoutException):
                            pass
                            break
                
                # shows where the selection of brands takes place (its finding is necessary) [# CHECK-BOX-1]
                show_brand = self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Бренды')]")))
                actions = ActionChains(driver)
                actions.move_to_element(show_brand).key_down(Keys.ARROW_DOWN).perform()
                ActionChains(self.driver).send_keys(Keys.ARROW_DOWN * 3).perform()
                self.highlight(show_brand)
                #
                # opens list of brands + text-box for search brands (this is optional)
                while 1==1:
                    try:
                        # opens list of brands
                        view_all = self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Бренды')]/parent::div//span[contains(text(),'Посмотреть все')]")))
                        actions = ActionChains(driver)
                        actions.move_to_element(view_all).perform()
                        ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
                        self.highlight(view_all)
                        webdriver.ActionChains(driver).click(view_all).perform()
                        #
                        # text-box for search brands
                        text_box_1 = self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Бренды')]/following-sibling::div//input[@type='text']")))
                        webdriver.ActionChains(driver).move_to_element(text_box_1).click(text_box_1).perform()
                        self.highlight(text_box_1)
                        webdriver.ActionChains(driver).move_to_element(text_box_1).send_keys(brand).perform()
                        time.sleep(1)
                        break
                    # if missing UI-elements, then script goes on
                    except (NoSuchElementException, TimeoutException):
                        pass
                        break
                        #
                # selects necessary check-box №1 (brand)
                check_box_1 = driver.find_element(By.XPATH,f"//div[contains(text(),'Бренды')]/following-sibling::div//input[@type='checkbox']/parent::label//span[contains(text(),'{brand}')]")             
                actions = ActionChains(driver)
                actions.move_to_element(check_box_1).perform()
                #
                self.highlight(check_box_1)
                time.sleep(2)
                driver.execute_script("arguments[0].click(true);", check_box_1)
                while 1==1:
                    try:
                        was_is_checked_box_1 = driver.find_element(By.XPATH,f"//div[contains(text(),'Бренды')]/following-sibling::div//input[@type='checkbox']/parent::label//span[contains(text(),'{brand}')]/ancestor::label/input")
                        self.assertTrue(was_is_checked_box_1.is_selected(), 'selected necessary check-box #1')
                        break
                    except StaleElementReferenceException:
                        pass
                        continue
                time.sleep(2)
                    
                # shows where sellers are selected (its finding is necessary) [# CHECK-BOX-2]
                show_seller = self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Продавец')]")))
                actions = ActionChains(driver)
                actions.move_to_element(show_seller).key_down(Keys.ARROW_DOWN).perform()
                ActionChains(self.driver).send_keys(Keys.ARROW_DOWN * 2).perform()
                self.highlight(show_seller)
                #
                # opens list of sellers + text-box for search sellers (this is optional)
                while 1==1:
                    try:
                        # opens list of sellers
                        view_all_1 = self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Продавец')]/parent::div//span[contains(text(),'Посмотреть все')]")))
                        actions = ActionChains(driver)
                        actions.move_to_element(view_all_1).perform()
                        ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
                        self.highlight(view_all_1)
                        webdriver.ActionChains(driver).click(view_all_1).perform()
                        #
                        # text-box for search sellers
                        text_box_2 = self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Продавец')]/following-sibling::div//input[@type='text']")))
                        webdriver.ActionChains(driver).move_to_element(text_box_2).click(text_box_2).perform()
                        self.highlight(text_box_2)
                        webdriver.ActionChains(driver).move_to_element(text_box_2).send_keys(seller).perform()
                        time.sleep(1)
                        break
                    # if missing UI-elements, then script goes on
                    except (NoSuchElementException, TimeoutException):
                        pass
                        break
                        #
                # selects necessary check-box №2 (seller)
                check_box_2 = driver.find_element(By.XPATH,f"//div[contains(text(),'Продавец')]/following-sibling::div//input[@type='checkbox']/parent::label//span[contains(text(),'{seller}')]")
                actions = ActionChains(driver)
                actions.move_to_element(check_box_2).key_down(Keys.ARROW_DOWN).perform()
                #
                self.highlight(check_box_2)
                time.sleep(2)
                driver.execute_script("arguments[0].click(true);", check_box_2)
                while 1==1:
                    try:
                        was_is_checked_box_2 = driver.find_element(By.XPATH,f"//div[contains(text(),'Продавец')]/following-sibling::div//input[@type='checkbox']/parent::label//span[contains(text(),'{seller}')]/ancestor::label/input")
                        self.assertTrue(was_is_checked_box_2.is_selected(), 'selected necessary check-box #2')
                        break
                    except StaleElementReferenceException:
                        pass
                        continue
                time.sleep(2)
                
                # setting the product price (this is optional) [# PRICE]
                setting_the_price = self.check_exists_by_xpath("//div[contains(text(),'Цена')]")
                if setting_the_price is True:
                    self.product_price_3()
                elif setting_the_price is False:
                    #
                    while 1==1:
                        try:
                            all_filters = driver.find_element(By.XPATH,"//span[contains(text(),'Все фильтры')]")
                            actions = ActionChains(driver)
                            actions.move_to_element(all_filters).key_down(Keys.ARROW_DOWN).perform()
                            time.sleep(2)
                            self.highlight(all_filters)
                            driver.execute_script("arguments[0].click(true);", all_filters)
                            time.sleep(2)
                            #
                            show_price_1 = self.wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Цена')]/parent::div/parent::div/parent::div")))
                            self.highlight(show_price_1)
                            price_opener = self.wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Цена')]/ancestor::div/*[name()='svg']"))).click()
                            time.sleep(2)
                            #
                            div = driver.find_element(by=By.XPATH, value="//span[contains(text(),'Цена')]//ancestor::"
                            + "div/following-sibling::div[contains(@class,'filter-block')] //div[@unit='[object Object]']/div[2]/div[2]")
                            self.highlight(div)
                            #
                            input_1 = self.wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Цена')]//ancestor::div/following-sibling::"
                            + "div[contains(@class,'filter-block')]//div[@unit='[object Object]']//p[contains(text(),'до')]/preceding-sibling::input"))).click()
                            time.sleep(2)
                            #        
                            actions = ActionChains(driver) 
                            actions.send_keys(Keys.BACKSPACE * 6).send_keys(price).perform()
                            ActionChains(driver).click(input_1).perform()
                            ActionChains(self.driver).key_down(Keys.ENTER).perform()
                            time.sleep(2)
                            #    
                            apply = driver.find_element(by=By.XPATH, value="//div/button/span/span[contains(text(),'Применить')]")
                            self.highlight(apply)
                            webdriver.ActionChains(driver).click(apply).perform()
                            time.sleep(2)
                            break
                        # if missing UI-elements, then script goes on 
                        except (NoSuchElementException, TimeoutException):
                            pass
                            break
            
                # down / up to this element:
                try:
                    advertising = self.check_exists_by_xpath("//div[contains(text(),'Реклама')]/parent::div/*[name()='svg']/parent::div/div[contains(text(),'Реклама')]")
                    #
                    while 1==1:
                        try:
                            if advertising is True:
                                delivers = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@data-widget='searchResultsFiltersActive']//div[1]//button/descendant::div/child::span")))
                                self.driver.execute_script("coordinates = arguments[0].getBoundingClientRect(); scrollTo(coordinates.x,coordinates.y); arguments[0].click();", delivers)
                                ActionChains(self.driver).move_to_element(delivers).click(delivers).send_keys(Keys.ARROW_DOWN * 8).perform()
                                time.sleep(1)
                                #
                            elif advertising is False:
                                delivers = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@data-widget='searchResultsFiltersActive']//div[1]//button/descendant::div/child::span")))
                                self.driver.execute_script("coordinates = arguments[0].getBoundingClientRect(); scrollTo(coordinates.x,coordinates.y); arguments[0].click();", delivers)
                                ActionChains(self.driver).move_to_element(delivers).click(delivers).send_keys(Keys.ARROW_DOWN * 6).perform()
                                time.sleep(1)
                            break
                        except StaleElementReferenceException:
                            pass
                            continue
                except (NoSuchElementException, TimeoutException):
                    pass
                
                # makes a screenshot for the report (pic №3) [showing selected filters]
                past_time = self.extract_current_time()
                step_forward = self.makes_screenshot()
                self.extract_current_time()
                self.makes_screenshot()
                                 
                # shows selected categories (these elements is optional to show)
                try:
                    driver.find_element(By.XPATH,"//div[@data-widget='searchResultsFiltersActive']//div[6]//button/descendant::div/child::span")
                    number_items = 5
                except (NoSuchElementException, TimeoutException):
                    pass
                    number_items = 4
                    #
                categories = [
                "//div[@data-widget='searchResultsFiltersActive']//div[1]//button/descendant::div/child::span",
                "//div[@data-widget='searchResultsFiltersActive']//div[2]//button/descendant::div/child::span",
                "//div[@data-widget='searchResultsFiltersActive']//div[3]//button/descendant::div/child::span",
                "//div[@data-widget='searchResultsFiltersActive']//div[4]//button/descendant::div/child::span",                
                "//div[@data-widget='searchResultsFiltersActive']//div[5]//button/descendant::div/child::span"           
                ]            
                # number_items = 5
                for i in range(number_items):
                    try:
                        items = driver.find_element(By.XPATH, categories[i])
                        self.highlight(items)
                    except (NoSuchElementException, TimeoutException):
                        pass
                ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
                time.sleep(1)

                """ Кнопка - [В корзину] (add) не появится если ранее этот 
                товар (product) уже был добавлен в корзину сайта, но при этом 
                кнопки - [-] / [+] для убавления / добавления товара в корзину
                нажиматься всё же будут. Поиск ниже идущего html-элемента - add 
                (В корзину) является обязательным к нажатию по моему тест-кейсу, 
                а не опциональным действием. Если эта кнопка не будет найдена, то 
                следовательно этот тест считается провальным по тест-кейсу."""
                
                # adds to product basket 
                add = driver.find_element(By.XPATH,"//*[contains(text(),'В корзину')]")
                actions = ActionChains(driver)
                actions.move_to_element(add).perform()
                ActionChains(self.driver).key_down(Keys.ARROW_DOWN).perform()
                self.highlight(add)
                driver.execute_script("arguments[0].click(true);", add)
                time.sleep(2)
                
                """ При всём при этом кнопка - [В корзину] (add) всё-таки может быть 
                видна если ранее в корзину был добавлен другой товар не из теста, но на 
                такой случай также имеются соответствующие проверки ниже по моему скрипту."""
                
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
                    
                # makes a screenshot for the report (pic №4)
                # [demonstration that button-[add] and button-[+] were pressed (+ qty_1 fixation)]
                past_time = self.extract_current_time()
                step_forward = self.makes_screenshot()
                self.extract_current_time()
                self.makes_screenshot()
                
                """ Далее идёт своего рода защита от несанкционированного попадания скрипта в пустую корзину, т. к.
                далее будет иметь место проверка на наличие в корзине определённого товара по его html-элементу, то
                возможен и такой вариант при котором, этот html-элемент всё же может присутствовать в корзине в виде
                ранее искомого пользователем товара (в нижней части страницы корзины, например как предложение или
                реклама и т. д.). Но если сейчас html-элемент значка количества товара в корзине найден не будет,
                то и дальше скрипт никуда более не пойдёт и поэтому поводу можно будет уже больше не переживать. """

                # checking, that quantity on counter is not zero + highlighting counter, if qty > 0 [if qty=1] (this is the
                # 0 - zero check before all the main checks, if this zero check is not passed, then others will not begin)
                quantity_1 = driver.find_element(by=By.XPATH, value=counter)
                if quantity_1.text == "0":
                    print("\n-----------------------------------------------------------------------------------")
                    print("")
                    print(Fore.MAGENTA + "Undetected element — it is verifiable counter for quantity" 
                          + f"\nproduct in basket, and obviously, that quantity counter = {quantity_1.text}.")
                    print("")
                    print(f"counter = '{counter}'")
                    print("")
                    raise NoSuchElementException # exception is called here, if qty = 0 [!!!]
                else:
                    pass
                    self.highlight(quantity_1) # quantity-1 highlighting
                    time.sleep(2)

                # checking, that product by basket in necessary quantity (but no more, than necessary)
                # 1 - first check (checking quantity by counter)
                if quantity_1.text == "2": # for first check should always be quantity counter = 2 (only - 2)
                    print("\n-----------------------------------------------------------------------------------")
                    print("")
                    print(Fore.GREEN + "1 - first check  = done!  (by counter necessary quantity product in basket)")
                    result_1 = True
                else:
                    print("\n-----------------------------------------------------------------------------------")
                    print("")
                    print(Fore.RED + "1 - first check  = error! (quantity by counter does not match stated)")
                    result_1 = False
                    
                # saves the value by quantity counter (from var quantity_1)
                save_value_qnt_1 = quantity_1.text
                 
                # сatches the current URL + decoding this URL
                current_url = str(driver.current_url)
                verifiable_url = urllib.parse.unquote(current_url)
                
                # presses button - [basket] + highlighting
                basket = driver.find_element(by=By.XPATH, value="//*[contains(text(),'Корзина')]")
                self.highlight(basket)
                basket.click()
                time.sleep(2)
                
                # check that we are in the basket
                cart_URL = "https://www.ozon.ru/cart"
                current_url_1 = str(driver.current_url)
                self.assertEqual(cart_URL, current_url_1)
                
                # сhecking the title of the basket
                self.assertEqual(driver.title,'OZON.ru - Моя корзина')

                # removes extra modal window (if advertisement)
                ActionChains(driver).key_down(Keys.ESCAPE).perform()
                time.sleep(2)
                
                # product + seller highlighting on web-page (because everyone products has seller)
                try:
                    item_1 = driver.find_element(by=By.XPATH, value=f"//*[contains(text(),'{product}')]")
                    self.highlight(item_1)
                    # item_2 = driver.find_element(by=By.XPATH, value=f"//*[contains(text(),'{seller}')]")
                    # self.highlight(item_2)
                except (NoSuchElementException, TimeoutException):
                    pass
                
                # states the name of the product 
                # straight in basket for check his:
                product = str("Масло трансмиссионное At-Matic D Fluid синтетическое, для АКПП , 1 л")

                # 2 - second check (that there is an order for a product and this product is in the basket)
                while 1==1:
            
                    element_1 = self.check_exists_by_xpath(f"//*[contains(text(),'{product}')]")
                    # element_2 = self.check_exists_by_xpath(f"//*[contains(text(),'{seller}')]")

                    if element_1 is True: # and element_2 is True:
                        try:
                            # write script
                            script = """alert(`Если видно это сообщение, то выбранный скриптом
товар находится в продуктовой корзине и кнопка - [Корзина]
была нажата. Заказ был создан и находится сейчас в статусе: «Ожидает оплаты».`)"""
                            # generate a alert via javascript
                            driver.execute_script(script)
                            time.sleep(8)
                            # ActionChains(driver).key_down(Keys.ENTER).perform()
                            alert_obj = driver.switch_to.alert
                            alert_obj.dismiss()
                        except UnexpectedAlertPresentException as e:
                            pass
                        print("")
                        print(Fore.GREEN + "2 - second check = done!  (order has been created and product is in basket)")
                        result_2 = True
                        break
                    else:
                        try:
                            # write script
                            script = """alert(`Failure! Если видно это сообщение, то нужный и запрашиваемый
по этому авто-тесту конкретный товар в продуктовой корзине 
обнаружен не был (!!!). При этом кнопка - [Корзина] всё же 
была нажата и заказ был создан, но товар находящийся сейчас 
в корзине явно не тот, что нужен для теста. Что-то пошло не 
так, как было запланировано, где-то произошла ошибка. Error!`)"""
                            # generate a alert via javascript
                            driver.execute_script(script)
                            time.sleep(8)
                            # ActionChains(driver).key_down(Keys.ENTER).perform()
                            alert_obj = driver.switch_to.alert
                            alert_obj.dismiss()
                        except UnexpectedAlertPresentException as e:
                            pass
                        print("")
                        print(Fore.RED + "2 - second check = error! (order has not been created and product is not in basket)")
                        result_2 = False
                        break
                time.sleep(1)
                
                # additional verification, that this product one we need:
                WTF = True
                try:
                    what_in_basket = driver.find_element(by=By.XPATH, value="//hr/parent::a/span/span[contains(text(),'Трансмиссионное масло Nissan')]")
                    what_in_basket_text = str(what_in_basket.text)
                    # self.assertIn(product, what_in_basket_text)
                    self.assertEqual(product, what_in_basket_text)
                except (NoSuchElementException, TimeoutException):
                    pass
                except AssertionError:
                    pass
                    WTF = False
                
                # makes a screenshot for the report (pic №5) 
                # [what's inside the basket + what's by quantity counter (qty_1)]
                past_time = self.extract_current_time()
                step_forward = self.makes_screenshot()
                self.extract_current_time()
                self.makes_screenshot()
                
                # goes clicking on combo-box + highlighting + select 
                # (this is element UI for removing or adding products)
                combo_box = driver.find_element(By.NAME,"filter")
                self.highlight(combo_box)
                combo_box.click()
                time.sleep(2)
                #
                # setup quantity counter on - 1 (by counter quantity_2 = 1) / removes excess products
                if random_number != 1 or random_number == 2:
                    ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
                    time.sleep(1)
                    ActionChains(driver).key_down(Keys.ARROW_UP).perform()
                    time.sleep(1)
                    ActionChains(driver).key_down(Keys.ENTER).perform()
                    time.sleep(2)
                #    
                # alternative choice goes at - 3 (by counter quantity_2 = 3) / adds more products 
                elif random_number == 2 or random_number == 1:
                    ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
                    time.sleep(1)
                    ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
                    time.sleep(1)
                    ActionChains(driver).key_down(Keys.ENTER).perform()
                    time.sleep(2)

                # quantity-2 highlighting
                quantity_2 = driver.find_element(by=By.XPATH, value=counter)
                self.highlight(quantity_2)
                time.sleep(2)
                
                # makes a screenshot for the report (pic №6) 
                # [first quantity (qty_1) has been changed to qty_2]
                past_time = self.extract_current_time()
                step_forward = self.makes_screenshot()
                self.extract_current_time()
                self.makes_screenshot()
                
                """ Если расположенный ниже элемент - 'discounted_price' (цена со скидкой) далее на html-странице корзины 
                найден не будет, то фактически это дефект на сайте OZON, т. к. ранее (выше по коду) при установке фильтров 
                был активирован тумблер - [Товары со скидкой] (это же можно увидеть и на собранном URL). Следовательно, все
                выбираемые скриптом товары после включения фильтра - [Товары со скидкой] должны идти уже с настройкой на то,
                что у них будет иметься скидка, а также то, что эти товары можно будет приобрести со скидкой по карте Ozon."""
                
                # extra fourth check (checking how the product price 
                # is added / multiplied when there are many products)
                #
                # calculates the cost of all products
                multi_price = int(price) * 3
                multi_price = str(multi_price)
                #
                # finds and extracts the price value
                try:
                    discounted_price = driver.find_element(by=By.XPATH, value="//div[2]//div/child::hr[contains(@style,'height:')]/following-sibling::div/div/child::span[contains(text(),'Картой')]")
                    self.highlight(discounted_price)
                    price_pulling = str(discounted_price.text).replace(" ", "")
                    stop = 4 # end position at slicing
                    slice_str = slice(stop)
                    extraction_result = price_pulling[slice_str]
                    if multi_price == extraction_result or price == extraction_result: # + checking how is the subtraction from multi-price correct
                        result_4 = True
                    else:
                        result_4 = False
                except (NoSuchElementException, TimeoutException):
                    pass
                    result_4 = False
                    extraction_result = Fore.MAGENTA + "None \n[Obviously, discounted price was not found on web-page (in basket).]\n"
                
                # test results (will be selected by script)
                test_result_1 = str("TEST SUCCESSFULLY (all available checks were successful)\n")
                test_result_2 = str("TEST partly SUCCESSFULLY (some of checks were not passed)\n")
                test_result_3 = str("TEST FAILED (because all available checks have been failed)\n")
                
                # declaring global variable (result_3)
                global result_3
                result_3 = True

                # checking that product was added in basket (or was remove from basket)
                # 3 - third check (changing quantity in fact)
                if quantity_2.text == "1":
                    print("")
                    print(Fore.GREEN + "3 - third check  = done!  (product was remove from basket / by default qty)")
                    print("\n-----------------------------------------------------------------------------------")
                    print("What values were used:")
                    print(f'price = "{price}"')
                    print(f'brand = "{brand}"')
                    print(f'seller = "{seller}"')
                    print(f'product = "{product}"') 
                    print("")
                    if save_value_qnt_1 == "2":
                        print("It is expected, that by counter quantity-1 = 2 (first check).")
                    else:
                        print(Fore.YELLOW + f"It is expected, that by counter quantity-1 = 2 only 2,\nbut by counter quantity-1 = {save_value_qnt_1} and it error (first check).\n")
                    print("It is expected, that by counter quantity-2 = 1 (third check).")
                    print("")
                    if result_4 == True:
                        print(f"Price of one product = {extraction_result} (fourth extra check).")
                    elif result_4 == False:
                        print(Fore.YELLOW + f"Price of one product is distorted \nand its value = {extraction_result} (extra fourth check).")
                    print("")
                    print("What was collected in the URL:")    
                    print(textwrap.fill(verifiable_url, 60))
                    # for (.bat) file start
                    print("----------------------------------------------------------------------")
                    if result_1 == True and result_2 == True and result_4 == True:
                        print(test_result_1)
                    elif result_1 == False or result_2 == False or result_4 == False:
                        print(test_result_2)
                elif quantity_2.text == "3":
                    print("")
                    print(Fore.GREEN + "3 - third check  = done!  (product was added in basket / alternative check)")
                    print("\n-----------------------------------------------------------------------------------")
                    print("What values were used:")
                    print(f'price = "{price}"')
                    print(f'brand = "{brand}"')
                    print(f'seller = "{seller}"')
                    print(f'product = "{product}"')
                    print("")
                    if save_value_qnt_1 == "2":
                        print("It is expected, that by counter quantity-1 = 2 (first check).")
                    else:
                        print(Fore.YELLOW + f"It is expected, that by counter quantity-1 = 2 only 2,\nbut by counter quantity-1 = {save_value_qnt_1} and it error (first check).\n")
                    print("It is expected, that by counter quantity-2 = 3 (third check).")
                    print("")
                    if result_4 == True:
                        print(f"Multi-price for three products = {extraction_result} (fourth extra check).")
                    elif result_4 == False:
                        print(Fore.YELLOW + f"Multi-price for three products is distorted \nand its value = {extraction_result} (extra fourth check).")
                    print("")
                    print("What was collected in the URL:")    
                    print(textwrap.fill(verifiable_url, 60))
                    # for (.bat) file start
                    print("----------------------------------------------------------------------")
                    if result_1 == True and result_2 == True and result_4 == True:
                        print(test_result_1)
                    elif result_1 == False or result_2 == False or result_4 == False:
                        print(test_result_2) 
                else:
                    result_3 = False
                    print("")
                    print(Fore.RED + "3 - third check  = error! (quantity by counter does not match stated)")
                    print("\n-----------------------------------------------------------------------------------")
                    print("What values were used:")
                    print(f'price = "{price}"')
                    print(f'brand = "{brand}"')
                    print(f'seller = "{seller}"')
                    print(f'product = "{product}"') 
                    print("")
                    if save_value_qnt_1 == "2":
                        print("It is expected, that by counter quantity-1 = 2 (first check).\n")
                    else:
                        print(Fore.YELLOW + f"It is expected, that by counter quantity-1 = 2 only 2,\nbut by counter quantity-1 = {save_value_qnt_1} and it error (first check).\n")
                    print(Fore.YELLOW + f"It is expected, that by counter quantity-2 = 1 or 3,\nbut by counter quantity-2 = {quantity_2.text} and it error (third check).")
                    print("")
                    print(Fore.YELLOW + "By counter required quantity of products for test has been \nviolated, so prices values do not matter" 
                          + f" (fourth extra check \nin this case is not performed / and wrong sum of prices = {extraction_result}).")
                    print("")
                    print("What was collected in the URL:")    
                    print(textwrap.fill(verifiable_url, 60))
                    # for (.bat) file start
                    print("----------------------------------------------------------------------")  
                    if result_3 != True and result_2 != False or result_1 != False or result_4 != False:
                        print(test_result_2)
                   
                # it's very-very bad results)    
                if result_1 == False and result_2 == False and result_3 == False and result_4 == False:
                    print(test_result_3)
                
                # additional information by test:    
                print(f"result_1 = {result_1}")
                print(f"result_2 = {result_2}")
                print(f"result_3 = {result_3}")
                print(f"result_4 = {result_4}")
                print("")
                if WTF == False:
                    print(f"WTF = {WTF}")
                    print(f"product = {product}")
                    print(f"what in basket: {what_in_basket_text}")
                    print("")

                # transition buying product
                execute = driver.find_element(by=By.XPATH, value="//*[contains(text(),'Перейти к оформлению')]")
                self.highlight(execute)
                execute.click()
                time.sleep(4)
                
                # makes a screenshot for the report (pic №7) [checkout screen]
                past_time = self.extract_current_time()
                step_forward = self.makes_screenshot()
                self.extract_current_time()
                self.makes_screenshot()
             
                # warning [!!!] (product quantity = 1)
                if one_unit != False:
                    print("")
                    print("")
                    print("")
                    print(Fore.MAGENTA + "======================= Attention! Attention! =======================")
                    print(Fore.MAGENTA + "The quantity of the required product on the website is only one unit!")
                    print(Fore.MAGENTA + "(required quantity product = 1 and 1 - first check cannot be passed)")
                    print(Fore.MAGENTA + "=====================================================================")
                    print("")
                    print("")
                
                basket_is_empty = True    
                self.checking_basket()
                break
            ################################################################################################################################################################################
            except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, JavascriptException, TimeoutException, ElementNotInteractableException) as ex:
                try:
                    # write script
                    script = "alert('Error! The requested html-element was not found on the web-page!')"
                    # generate a alert via javascript
                    driver.execute_script(script)
                    time.sleep(5)
                    ActionChains(driver).key_down(Keys.ENTER).perform()
                except UnexpectedAlertPresentException as e:
                    pass
                print("\n-----------------------------------------------------------------------------------")
                print(Fore.RED + "Error! The requested html-element was not found on the web-page!")
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

                self.PrintException()
                print("")
                print("Exception type: %s" %ex_type.__name__)
                print("")
                # print("Exception message: %s" %ex_value)
                print(f"Exception message:\n{ex.msg}")
                # log.logger.exception(f"Exception message: {ex.msg}", exc_info=False)
                # print("")
                # print("Stack trace: %s" %stack_trace)
                
                # for (.bat) file start / or alternative
                print("----------------------------------------------------------------------") 
                print("TEST FAILED (the requested html-element was not found on the web-page)\n") 
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
                if basket_is_empty == True:
                    # print(f"basket_is_empty = {basket_is_empty}")
                    self.assertTrue(self.is_element_present(By.XPATH,f"//*[contains(text(),'{product}')]"), 'product inside the basket')
                    # self.assertTrue(self.is_element_present(By.XPATH,f"//*[contains(text(),'{seller}')]"), 'seller inside the basket')
                elif basket_is_empty == False:
                    pass
                
                # button-1
                del_1 = str("//*[contains(text(),'Удалить выбранные')]")

                # button-2
                del_2 = str("//div[contains(text(),'Отменить')]/following-sibling::div//span[contains(@style,'border-radius:')]/span[text()='Удалить']")
                
                # checks if there is + presses button - [delete ALL] (opens modal window)
                self.assertTrue(self.is_element_present(By.XPATH, del_1), 'is available button - [delete ALL]')
                delete_ALL = self.wait.until(EC.presence_of_element_located((By.XPATH, del_1))).click()

                # checks if there is + presses button - [delete] (removes all products and counter)
                self.assertTrue(self.is_element_present(By.XPATH, del_2), 'is available button - [delete]')
                delete_2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, del_2)))
                driver.execute_script("arguments[0].click(true);", delete_2)
                # time.sleep(1)
                
                # checking that the basket is empty
                self.assertTrue(self.is_element_present(By.XPATH,"//h1[text()='Корзина пуста']"), 'that the basket is empty')
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