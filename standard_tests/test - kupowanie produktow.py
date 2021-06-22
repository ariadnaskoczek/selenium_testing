import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time

#Dane testowe
valid_emaial="testerwsb2021@gmail.com"
valid_password = "webtester"
product="Perfumy"
name="Marianna"
surname="Kowalska"
phone="564567456"
adress="Kozia 5"
town="Kozia Wolka"


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

    def test_buying_product(self):
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
        print("chooing brand of perfum")
        search_btn = driver.find_element_by_class_name('_2wKvURHJBZWGavg_Gquwn3')
        search_btn.click()
        print("brand_list")
        brand=driver.find_element_by_xpath("//div[@id='ca-uid-4']")
        brand.click()
        print("choosing brand")
        Brand_of_perfum=driver.find_element_by_xpath("//span[text()='Ariana Grande']")
        Brand_of_perfum.click()
        print("list of fragrance note")
        fragrance_note=driver.find_element_by_xpath("//div[@id='ca-uid-5']")
        fragrance_note.click()
        print("choosing note")
        flowers_checkbox=driver.find_element_by_xpath("//span[text()='Kwiatowe']")
        flowers_checkbox.click()
        time.sleep(10)
        print("choosing discount")
        discount=driver.find_element_by_xpath("//div[@id='ca-uid-5']")
        discount.click()
        print("free delivery")
        free_delivery_checkbox=driver.find_element_by_class_name('checkbox__value')
        free_delivery_checkbox.click()
        #POP
        print("choosing product")
        click_product = driver.find_element_by_xpath("//strong[text()='Ari by Ariana Grande']")
        click_product.click()
        print("adding the product to shopping cart")
        add_button = driver.find_element_by_class_name('sc-eirqVv')
        # add_button = driver.find_element_by_class_name('sc-fznyYp')
        add_button.click()
        time.sleep(3)
        print("continue shopping")
        btn_continue_shopping=driver.find_element_by_id('upsellingContinueWithShopping')
        btn_continue_shopping.click()
        print("going to shopping card")
        btn_shopping_card=driver.find_element_by_class_name('_2NAJ4Yecy7V8XjwTR42jYF')
        btn_shopping_card.click()
        print("removing product")
        remove_product=driver.find_element_by_id('removeFromBasket_15675800')
        remove_product.click()

    def tearDown(self):
        print("Sprzątanie po teście")
        #Wyłączamy przeglądarkę
        self.driver.quit()


        







