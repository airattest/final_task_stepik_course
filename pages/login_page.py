from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This page is not intended for login or registration."
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.should_be_login_form), "There is no login form"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.should_be_register_form), "There is no registration form"
        assert True
