from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart_code(self):
        basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_LINK)
        basket_link.click()

    def add_to_cart_success(self):
        success_text = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        success = success_text.text
        assert "The shellcoder's handbook" == success, "Error"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"