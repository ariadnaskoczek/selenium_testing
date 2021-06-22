from my_project.page_object_pattern.pages.base_page import BasePage
from my_project.page_object_pattern.locators import LoginPageLocators

class LoginPage(BasePage):

    def fill_email(self, email):
        print("filling email:", email)
        putin_email = self.driver.find_element(*LoginPageLocators.email)
        putin_email.send_keys(email)

    def fill_password(self, password):
        print("filling password:", password)
        putin_password = self.driver.find_element(*LoginPageLocators.password)
        putin_password.send_keys(password)

    def press_approve_button(self):
        print("pressing button")
        approved_btn = self.driver.find_element(*LoginPageLocators.approved_btn)
        approved_btn.click()