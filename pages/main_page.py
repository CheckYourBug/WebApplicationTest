from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
class MainPage(BasePage):
    #метод даёт ссылку на элемент входа
    #соответственно называем логично
    #доступ к BasePage и его методм передается через self
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
