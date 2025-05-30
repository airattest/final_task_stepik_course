from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        self.browser.find_element(*LoginPageLocators.REG_FIELD_INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_FIELD_INPUT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_FIELD_INPUT_PASSWORD_RETRY).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This page is not intended for login or registration."
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.SHOULD_BE_LOGIN_FORM), "There is no login form"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SHOULD_BE_REGISTER_FORM), "There is no registration form"
        assert True
