import pytest
from pages.main_page import MainPage
from pages.basket_page import BasketPage
@pytest.mark.skip
def test_guest_go_to_login_page(browser):
    #создаем переменную page которая имеет доступ к классу MainPage, а тот наследник BasePage
    #имеет доступ к методам обоих классов
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, link)
    page.should_not_be_goods_in_basket()
    page.should_basket_be_empty()


