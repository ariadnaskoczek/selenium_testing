import time

from my_project.page_object_pattern.locators import ProductPageLocators
from my_project.page_object_pattern.pages.base_page import BasePage


class ProductPage (BasePage):

    def putting_product(self, product):
        print("putting product", product)
        el = self.driver.find_element(*ProductPageLocators.product_input)
        el.send_keys(product)

    def click_search_btn(self):
        print("choosing brand of perfume")
        el = self.driver.find_element(*ProductPageLocators.search_btn)
        el.click()

    def open_brand_list(self):
        print("open brand list")
        el= self.driver.find_element(*ProductPageLocators.perfume_list)
        el.click()

    def chose_Brand_of_perfum(self):
        print("choosing brand")
        el=self.driver.find_element(*ProductPageLocators.ariadne_grande_perfume)
        el.click()

    def displaying_fragrance_note_of_perfume(self):
        print("list of fragrance note")
        el= self.driver.find_element(*ProductPageLocators.fragrance_note)
        el.click()

    def choice_of_fragrance_note_of_perfume(self):
        print("choosing note")
        el = self.driver.find_element(*ProductPageLocators.flowers_checkbox)
        el.click()

    def choice_of_discount(self):
        print("choosing discount")
        el=self.driver.find_element(*ProductPageLocators.discount_checkbox)
        el.click()

    def choice_of_free_deliver(self):
        print("choosing free delivery")
        el=self.driver.find_element(*ProductPageLocators.free_delivery_checkbox)
        el.click()
        time.sleep(3)

    def final_choice_of_product(self):
        print("final choice of product")
        el=self.driver.find_element(*ProductPageLocators.click_product)
        el.click()

    def add_product_to_the_cart(self):
        print("adding the product to shopping cart")
        el=self.driver.find_element(*ProductPageLocators.add_button)
        el.click()

    def continuation_of_shopping(self):
        print("continue shopping")
        el=self.driver.find_element(*ProductPageLocators.btn_continue_shopping)
        el.click()

    def go_to_the_cart(self):
        print("going to shopping cart")
        el=self.driver.find_element(*ProductPageLocators.btn_shopping_cart)
        el.click()

    def resignation_from_the_product(self):
        print("removing product")
        el=self.driver.find_element(*ProductPageLocators.remove_product)
        el.click()


