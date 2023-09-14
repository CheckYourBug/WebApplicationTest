from pages.book_page import BookPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import faker
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = BookPage(browser, link)
    page.open()
    page.should_add_to_basket()
    page.solve_and_get_code()
    page.should_book_name()
    page.should_book_price()
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BookPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BookPage(browser, link)
    page.open()
    page.go_to_login_page()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BookPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, link)
    page.should_not_be_goods_in_basket()
    page.should_basket_be_empty()
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        em = faker.Faker()
        page.register_new_user(email=em.email(), password="dgkforever")
        page.should_be_authorized_user()
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = BookPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = BookPage(browser, link)
        page.open()
        page.should_add_to_basket()
        page.should_book_name()
        page.should_book_price()



