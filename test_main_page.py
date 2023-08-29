from pages.main_page import MainPage
link = "http://selenium1py.pythonanywhere.com/"
def test_guest_go_to_login_page(browser):
    #создаем переменную page которая имеет доступ к классу MainPage, а тот наследник BasePage
    #имеет доступ к методам обоих классов
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
