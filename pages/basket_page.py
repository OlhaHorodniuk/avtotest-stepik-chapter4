from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty_message(self):
        assert self.is_not_element_present(*BasketPageLocators.TABLE_PRODUCT), "Item in basket"

    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET), "Basket is not empty"