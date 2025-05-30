from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART), "Shopping cart there are products"

    def item_in_the_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IS_IN_THE_CART), "There is no product in the Cart"
