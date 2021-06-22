from selenium.webdriver.common.by import By


class HomePageLocators():
    """ Selektory strony głównej"""
    login_btn = (By.CLASS_NAME, '_1W8FHoGkAK1-vShN-OLaxj')


class LoginPageLocators():
    """ Selektory strony Logowanie"""
    email = (By.ID, 'login-name')
    password = (By.ID, 'login-pwd')
    approved_btn = (By.XPATH, '//button[@type="submit"]')


class ProductPageLocators():
    """Selektory ze strony z produktami """
    product_input = (By.CLASS_NAME, '_2qwXK-vv7lFlvT83sBDFtt')
    search_btn = (By.CLASS_NAME,'_2wKvURHJBZWGavg_Gquwn3')
    perfume_list = (By.XPATH, '//div[@id="ca-uid-4"]')
    ariadne_grande_perfume = (By.XPATH, "//span[text()='Ariana Grande']")
    fragrance_note = (By.XPATH,"//div[@id='ca-uid-5']")
    flowers_checkbox=(By.XPATH,"//span[text()='Kwiatowe']")
    discount_checkbox = (By.XPATH, "//div[@id='ca-uid-5']")
    free_delivery_checkbox=(By.CLASS_NAME,'checkbox__value')
    add_button = (By.CLASS_NAME,'sc-eirqVv')
    click_product = (By.XPATH,"//strong[text()='Ari by Ariana Grande']")
    btn_continue_shopping = (By.ID,'upsellingContinueWithShopping')
    btn_shopping_cart=(By.CLASS_NAME,'_2NAJ4Yecy7V8XjwTR42jYF')
    remove_product=(By.ID,'removeFromBasket_15675800')


class PaymentPageLocators():
    product_input = (By.CLASS_NAME, '_2qwXK-vv7lFlvT83sBDFtt')
    search_btn = (By.CLASS_NAME,'_2wKvURHJBZWGavg_Gquwn3')
    click_product = (By.XPATH,"//strong[text()='2000 Calorie Curl Addict']")
    add_button = (By.CLASS_NAME,'sc-eirqVv')
    btn_shopping_cart=(By.XPATH,"//a[@data-cypress='goToShoppingCart']")
    checkbox_value =(By.CLASS_NAME,'checkbox__value')
    btn_cash_register = (By.ID,'submit_next_2b')
    btn_goahead= (By.ID,'submit_next_3a')
    btn_Nextstep= (By.ID, 'submit_next_5')
    input_name =(By.ID,'delivery-name')
    input_surname = (By.ID,'delivery-surname')
    btn_buy_now = (By.ID,'submit_order')
