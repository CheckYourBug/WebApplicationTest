from selenium.webdriver.common.by import By
class MainPageLocators():
    #каждая переменная - пара: (как искать, "что искать (селектор)")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    SECOND_PASS_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
class BookPageLocators():
    BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner>strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner>p>strong")
    BOOK_NAME = (By.CSS_SELECTOR, "div>h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span>a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class BasketPageLocators():
    GOODS_IN_BASKET = (By.CSS_SELECTOR, "h2.col-sm-6")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")





