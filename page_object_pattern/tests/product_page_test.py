from my_project.page_object_pattern.pages.home_page import HomePage
from my_project.page_object_pattern.pages.login_page import LoginPage
from my_project.page_object_pattern.pages.product_page import ProductPage
from my_project.page_object_pattern.tests.base_page_test import BaseTest
from my_project.page_object_pattern.pages.payment_page import PaymentPage
import time
product_1 = "perfumy"
product_2="Max Factor 2000 Calorie Curl Addict"
email = "testerwsb2021@gmail.com"
password ="webtester"
name = "Marianna"
surname = "Kowalska"
phone ="564567456"
adress ="Kozia 5"
town ="Kozia Wolka"


class TestProduct(BaseTest):

    def test_buying_product(self):
        # home page
        hp = HomePage(self.driver)
        hp.click_login_btn()
        # logging in
        lp = LoginPage(self.driver)
        lp.fill_email(email)
        lp.fill_password(password)
        lp.press_approve_button()
        #buying product
        pp = ProductPage(self.driver)
        pp.putting_product(product_1)
        pp.click_search_btn()
        pp.open_brand_list()
        pp.chose_Brand_of_perfum()
        pp.displaying_fragrance_note_of_perfume()
        pp.choice_of_fragrance_note_of_perfume()
        pp.choice_of_discount()
        pp.choice_of_free_deliver()
        pp.final_choice_of_product()
        pp.add_product_to_the_cart()
        pp.continuation_of_shopping()
        pp.go_to_the_cart()
        pp.resignation_from_the_product()

    def test_payment(self):
        # home page
        hp = HomePage(self.driver)
        hp.click_login_btn()
        # logging in
        lp = LoginPage(self.driver)
        lp.fill_email(email)
        lp.fill_password(password)
        lp.press_approve_button()
        #product page
        pp = ProductPage(self.driver)
        pp.putting_product(product_2)
        pp.click_search_btn()
        pt = PaymentPage(self.driver)
        pt.click_product()
        pt.add_product_to_shopping_cart()
        pt.click_shopping_cart_btn()
        pt.mark_eco_box()
        pt.go_to_cash_register()
        pt.click_btn_go_ahead()
        pt.go_to_next_step()
        pt.input_name(name)
        pt.input_surname(surname)
        pt.submit_order()






