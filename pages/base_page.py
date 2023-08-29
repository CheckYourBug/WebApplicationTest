from selenium.common.exceptions import NoSuchElementException
url = "http://selenium1py.pythonanywhere.com/"
class BasePage():
    #метод init
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self):
        self.browser.get(self.url)
    #создаем метод осмысленного сообщения об ошибке в случае не нахождения элемента
    #how - метод поиска (css, xpath, byid etc.), what - само значение селектора
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True