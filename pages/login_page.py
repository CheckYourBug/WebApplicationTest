from .base_page import BasePage
from .locators import LoginPageLocators
class LoginPage(BasePage):
    def should_be_login_page(self, browser):
        self.should_be_login_url(browser)
        self.should_be_login_form()
        self.should_be_register_form()
    def should_be_login_url(self, browser):
        # реализуйте проверку на корректный url адрес
        assert "login" in browser.current_url, "Incorrect url"
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no Login form on the page"
    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "There is no Registration form on the page"