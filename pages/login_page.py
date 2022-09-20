from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not found login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email = self.browser.find_element(By.CSS_SELECTOR, "input#id_registration-email")
        email_text = str(time.time()) + "@fakemail.org"
        email.send_keys(email_text)
        password1 = self.browser.find_element(By.CSS_SELECTOR, "input#id_registration-password1")
        password1.send_keys('dfghfg34dgdfAA')
        password2 = self.browser.find_element(By.CSS_SELECTOR, "input#id_registration-password2")
        password2.send_keys('dfghfg34dgdfAA')
        button = self.browser.find_element(By.CSS_SELECTOR, "form#register_form button")
        button.click()