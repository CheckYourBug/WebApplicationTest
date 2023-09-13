from .base_page import BasePage
from .locators import BookPageLocators
from .locators import BasePageLocators

class BookPage(BasePage):
    def should_add_to_basket(self):
        basket = self.browser.find_element(*BookPageLocators.BASKET)
        basket.click()
        #alert = self.browser.switch_to.alert
        #alert.accept()
    def should_book_name(self):
        added_book_name = self.browser.find_element(*BookPageLocators.ADDED_BOOK_NAME).text
        book_name = self.browser.find_element(*BookPageLocators.BOOK_NAME).text
        assert added_book_name == book_name, "wrong book added"
    def should_book_price(self):
        basket_price = self.browser.find_element(*BookPageLocators.BASKET_PRICE).text
        book_price = self.browser.find_element(*BookPageLocators.BOOK_PRICE).text
        assert basket_price == book_price, "wrong price of basket"
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BookPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    def should_disappeared_seccess_massage(self):
        assert self.is_disappeared(*BookPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
