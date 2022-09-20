from .base_page import BasePage
from .main_page import MainPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_cart_code(self):
        basket_link = self.browser.find_element(*MainPageLocators.ADD_TO_CART_LINK)
        basket_link.click()

    def add_to_cart_success(self):
        success_text = self.browser.find_element(By.CSS_SELECTOR, 'div.alertinner strong')
        success = success_text.text
        assert "Coders at Work" == success, "Error"
