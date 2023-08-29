from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
class MainPage(BasePage):
    #метод даёт ссылку на элемент входа
    #доступ к BasePage и его методм передается через self
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not on the page"
