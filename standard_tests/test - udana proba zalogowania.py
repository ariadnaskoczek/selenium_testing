import unittest
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

#Dane testowe
valid_emaial="ariadna.skoczek1991@gmail.com"
valid_password = "webtester2021"
class Login (unittest.TestCase):
    def setUp(self):
        #warunki wstepne testow:
        #wlaczamy przegladarke i strone
        print("Przygotowanie testu.")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.get('https://www.notino.pl/')
        time.sleep(5)

    def testEmail(self):
        print("Prawdziwy test")
        driver = self.driver
        time.sleep(10)
        #odszukanie zakladki "zaloguj sie"
        login_btn = driver.find_element_by_class_name('_1W8FHoGkAK1-vShN-OLaxj')
        login_btn.click()
        time.sleep(10)
        print("putting email")
        putin_email= driver.find_element_by_id('login-name')
        putin_email.send_keys(valid_emaial)
        print("putting password")
        putin_password=driver.find_element_by_id('login-pwd')
        putin_password.send_keys(valid_password)
        print("pressing button")
        approved_btn=driver.find_element_by_xpath("//button[@type='submit']")
        approved_btn.click()
        time.sleep(10)
