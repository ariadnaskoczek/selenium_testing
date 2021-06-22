import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time

#Dane testowe
valid_emaial="testerwsb2021@gmail.com"
valid_password = "webtester"
product="Max Factor 2000 Calorie Curl Addict"
name="Marianna"
surname="Kowalska"



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

    def test_adding_product_to_basket(self):
        print("Prawdziwy test")
        driver = self.driver
        print("Finding 'zaloguj sie' tab")
        login_btn = driver.find_element_by_class_name('_1W8FHoGkAK1-vShN-OLaxj')
        login_btn.click()
        time.sleep(1)
        print("putting email")
        putin_email = driver.find_element_by_id('login-name')
        putin_email.send_keys(valid_emaial)
        print("putting password")
        putin_password = driver.find_element_by_id('login-pwd')
        putin_password.send_keys(valid_password)
        print("pressing button")
        approved_btn = driver.find_element_by_xpath("//button[@type='submit']")
        approved_btn.click()
        print("puttig product")
        putin_product = driver.find_element_by_class_name('_2qwXK-vv7lFlvT83sBDFtt')
        putin_product.send_keys(product)
        print("pressing button : Search")
        search_btn = driver.find_element_by_class_name('_2wKvURHJBZWGavg_Gquwn3')
        search_btn.click()
        print("choosing product")
        click_product = driver.find_element_by_xpath("//strong[text()='2000 Calorie Curl Addict']")
        click_product.click()
        print("adding the product to shopping cart")
        add_button=driver.find_element_by_class_name('sc-eirqVv')
        #add_button = driver.find_element_by_class_name('sc-fznyYp')
        add_button.click()
        print("going to the shopping cart ")
        btn_shopping_cart = driver.find_element_by_xpath("//a[@data-cypress='goToShoppingCart']")
        btn_shopping_cart.click()
        time.sleep(4)
        print("uncheckboxing")
        checkbox_value = driver.find_elements_by_class_name('checkbox__value')[1]
        checkbox_value.click()
        time.sleep(3)
        print("going to the cash register ")
        btn_cash_register = driver.find_element_by_id('submit_next_2b')
        btn_cash_register.click()
        time.sleep(2)
        print("goahead")
        btn_goahead=driver.find_elements_by_class_name('r')[0]
        btn_goahead.click()
        print("Button Next_Step")
        btn_Nextstep=driver.find_element_by_id('submit_next_5')
        btn_Nextstep.click()
        time.sleep(10)
        print("inputting name")
        input_name=driver.find_element_by_id('delivery-name')
        input_name.send_keys(name)
        print("inputing surname")
        input_surname=driver.find_element_by_id('delivery-surname')
        input_surname.send_keys(surname)
        btn_buy_now=driver.find_element_by_id('submit_order')
        btn_buy_now.click()

    def tearDown(self):
        print("Sprzątanie po teście")
        # Wyłączamy przeglądarkę
        self.driver.quit()







