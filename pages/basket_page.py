from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET), \
            "Goods in basket is presented, but should not be"
    def should_basket_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Basket in not empty"

