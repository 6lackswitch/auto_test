from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "header span a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner strong')
    ADD_TO_CART_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")