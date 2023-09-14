from .base_page import BasePage
from .locators import LoginPageLocators
class LoginPage(BasePage):
    def register_new_user(self, email, password):
        link = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        link.send_keys(email)
        link = self.browser.find_element(*LoginPageLocators.PASS_FIELD)
        link.send_keys(password)
        link = self.browser.find_element(*LoginPageLocators.SECOND_PASS_FIELD)
        link.send_keys(password)
        link = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        link.click()
    def should_be_login_page(self, browser):
        self.should_be_login_url(browser)
        self.should_be_login_form()
        self.should_be_register_form()
    def should_be_login_url(self, browser):
        assert "login" in browser.current_url, "Incorrect url"
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no Login form on the page"
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "There is no Registration form on the page"
