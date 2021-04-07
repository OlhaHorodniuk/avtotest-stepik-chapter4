from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        product_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        product_link.click()
        self.solve_quiz_and_get_code()

    def does_the_title_of_the_book_match(self):
        book_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        book_name = book_name.text
        alert_book_name = self.browser.find_element(*ProductPageLocators.ALERT_NAME_PRODUCT)
        alert_book_name = alert_book_name.text
        assert book_name == alert_book_name, \
            f"The book {book_name} was not added to the cart"

    def does_the_price_of_the_book_match(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        book_price = book_price.text
        alert_book_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE_PRODUCT)
        alert_book_price = alert_book_price.text
        assert book_price == alert_book_price, \
            f"The price {book_price} of the book does not match the price in the basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_NAME_PRODUCT), \
            "Success message for added product is displayed, but should not"

    def should_disappeared_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_NAME_PRODUCT), \
            "Success message for added product is displayed, but should not"



