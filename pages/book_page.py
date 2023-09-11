from .base_page import BasePage
from .locators import BookPageLocators
import time
import math
import pyperclip
from selenium.common.exceptions import NoAlertPresentException
class BookPage(BasePage):
    def should_add_to_basket(self):
        basket = self.browser.find_element(*BookPageLocators.BASKET)
        basket.click()
        #alert = self.browser.switch_to.alert
        #alert.accept()
    def should_book_name(self):
        name = self.browser.find_element(*BookPageLocators.BOOKNAME).text
        assert name == "The shellcoder's handbook", "wrong book added"
    def should_book_price(self):
        price = self.browser.find_element(*BookPageLocators.BOOKPRICE).text
        assert price == "9,99 £", "wrong price of basket"
