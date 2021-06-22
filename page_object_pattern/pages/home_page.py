from my_project.page_object_pattern.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from my_project.page_object_pattern.locators import HomePageLocators

class HomePage(BasePage):
    """
    Strona domowa
    """

    def click_login_btn(self):
        el = self.driver.find_element(*HomePageLocators.login_btn)
        el.click()

    def _verify_page(self):
        # Weryfikuję, czy strona ma poprawny tytuł
        # Czekam na przycisk "ZALOGUJ"
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(HomePageLocators.login_btn))
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(HomePageLocators.login_btn))
        assert "Perfumy i kosmetyki online" in self.driver.title
        print("Weryfikacja strony HomePage")