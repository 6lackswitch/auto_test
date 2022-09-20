from .base_page import BasePage
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_not_be_product_in_cart(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, "div.basket-title.hidden-xs"), \
            "Product in cart, but must empty"
    
    def should_be_message_empty_cart(self):
        text_message = self.browser.find_element(By.CSS_SELECTOR, "div.content p")
        text = text_message.text
        assert "Your basket is empty" in text, "Product cart must be empty"