import time

from my_project.page_object_pattern.locators import PaymentPageLocators
from my_project.page_object_pattern.pages.base_page import BasePage

class PaymentPage (BasePage):

    def put_product(self, product):
        print("putting product", product)
        el = self.driver.find_element(*PaymentPagePageLocators.product_input)
        el.send_keys(product)

    def search_btn(self):
        print("wpisywanie produktu")
        el = self.driver.find_element(*PaymentPagePageLocators.click_search_btn)
        el.click()

    def click_product(self):
        print("wybieranie produktu")
        el =self.driver.find_element(*PaymentPageLocators.click_product)
        el.click()

    def add_product_to_shopping_cart(self):
        print("adding the product to shopping cart")
        el = self.driver.find_element(*PaymentPageLocators.add_button)
        el.click()

    def click_shopping_cart_btn(self):
        print("going to the shopping cart ")
        el= self.driver.find_element(*PaymentPageLocators.btn_shopping_cart)
        el.click()

    def mark_eco_box(self):
        print("marking eco box for delivery")
        el = self.driver.find_elements(*PaymentPageLocators.checkbox_value)[1]
        el.click()

    def go_to_cash_register(self):
        print("going to the cash register ")
        el=self.driver.find_element(*PaymentPageLocators.btn_cash_register)
        el.click()

    def click_btn_go_ahead(self):
        print("clicking btn go_ahead")
        el=self.driver.find_element(*PaymentPageLocators.btn_goahead)
        el.click()

    def go_to_next_step(self):
        print("clicking btn go_to_next_step")
        el= self.driver.find_element(*PaymentPageLocators.btn_Nextstep)
        el.click()

    def input_name(self, name):
        print("inputting name")
        el=self.driver.find_element(*PaymentPageLocators.input_name)
        el.send_keys(name)

    def input_surname(self, surname):
        print("inputing surname")
        el= self.driver.find_element(*PaymentPageLocators.input_surname)
        el.send_keys(surname)

    def submit_order(self):
        el= self.driver.find_element_by_id('submit_order')
        el.click()