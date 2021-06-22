import unittest

from my_project.page_object_pattern.pages.home_page import HomePage
from my_project.page_object_pattern.pages.login_page import LoginPage
from my_project.page_object_pattern.tests.base_page_test import BaseTest

email = "testerwsb2021@gmail.com"
password ="webtester"


class LoginTest(BaseTest):
    """
    Testy strony Rejestracja
    """
    def test_correct_email(self):
        """Test logowania - błędne haslo"""
        hp = HomePage(self.driver)
        hp.click_login_btn()
        lp = LoginPage(self.driver)
        lp.fill_email(email)
        lp.fill_password(password)
        lp.press_approve_button()

if __name__=="__main__":
    unittest.main(verbosity=2)

