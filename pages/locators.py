from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    SHOULD_BE_LOGIN_FORM = ("xpath", "(//h2)[1]")
    SHOULD_BE_REGISTER_FORM = ("xpath", "(//h2)[2]")
    THE_USER_IS_REGISTERED= ("xpath", "//i[@class='icon-user']")
    REG_FIELD_INPUT_EMAIL = ("xpath", "//input[@id='id_registration-email']")
    REG_FIELD_INPUT_PASSWORD = ("xpath", "//input[@id='id_registration-password1']")
    REG_FIELD_INPUT_PASSWORD_RETRY = ("xpath", "//input[@id='id_registration-password2']")
    REG_BUTTON = ("xpath", "//button[@name='registration_submit']")

class ProductPageLocators(object):
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = ("xpath", "(//div/strong)[3]")
    PRODUCT_NAME = ("xpath", "//h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    VIEW_CART = ("xpath", "//a[@class='btn btn-default']")
    EMPTY_CART = ("xpath", "//div[@id='content_inner']/p")
    PRODUCT_IS_IN_THE_CART= ("xpath", "//h2[@class='col-sm-6 h3']")
