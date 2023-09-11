from pages.book_page import BookPage
def test_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BookPage(browser, link)
    page.open()
    page.should_add_to_basket()
    page.solve_and_get_code()
    page.should_book_name()
    page.should_book_price()

