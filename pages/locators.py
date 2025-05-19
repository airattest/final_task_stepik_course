from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    SHOULD_BE_LOGIN_FORM = ("xpath", "(//h2)[1]")
    SHOULD_BE_REGISTER_FORM = ("xpath", "(//h2)[2]")
