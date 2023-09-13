from pages.book_page import BookPage
import pytest
@pytest.mark.parametrize('offer', ["0","1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    page = BookPage(browser, link)
    page.open()
    page.should_add_to_basket()
    page.solve_and_get_code()
    page.should_book_name()
    page.should_book_price()

