# -*- coding: utf-8 -*-
import sys
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

options = webdriver.ChromeOptions() 
options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data')
s = Service('C:\\chromedriver\\chromedriver.exe')

class BuyLeads(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=s, options=options)
        self.driver.implicitly_wait(2) # for so many seconds, he searches for the HTML element
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_buy_leads(self):
        try:
            driver = self.driver
            # Go to the page to buy leads
            driver.get("https://advert.apileads.tech/lead/")
            wait = WebDriverWait(driver, 10)
            time.sleep(1)
    
            def check_exists_by_xpath(xpath):
                try:
                    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                except NoSuchElementException as e: return False
                return True

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
                print("1 - first check = done! (order has been created)")
            else:
                print("1 - first check = error!")
        
            # 2 - second check
            while 1==1:
                
                element = check_exists_by_xpath("//*[contains(text(),'Заказ ID')]")

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
                    print("2 - second check = done! (order has been created)")
                    break
                else:
                    print("2 - second check = error!")
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
                print("3 - third check = done! (order is paid)")
            else:
                print("3 - third check = error!")
        
            # 4 - fourth check
            while 1==1:
                
                element = check_exists_by_xpath("//*[contains(text(),'Заказ оплачен')]")

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
                    print("4 - fourth check = done! (order is paid)")
                    break
                else:
                    print("4 - fourth check = error!")
                    break

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
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def exception_handler(exception_type, exception, traceback):
            # All your trace are belong to us!
            # your format
            print(exception_type.__name__, exception)
            
    sys.excepthook = exception_handler   
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

