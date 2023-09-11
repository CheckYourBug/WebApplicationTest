from selenium.webdriver.common.by import By
class MainPageLocators():
    #каждая переменная - пара: (как искать, "что искать (селектор)")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
class BookPageLocators():
    BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOKNAME = (By.CSS_SELECTOR, ".alertinner>strong")
    BOOKPRICE = (By.CSS_SELECTOR, ".alertinner>p>strong")



