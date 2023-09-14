from pages.book_page import BookPage
import pytest
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BookPage(browser, link)
    page.open()
    page.should_add_to_basket()
    page.should_not_be_success_message()
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BookPage(browser, link)
    page.open()
    page.should_not_be_success_message()
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BookPage(browser, link)
    page.open()
    page.should_add_to_basket()
    page.should_disappeared_seccess_massage()


