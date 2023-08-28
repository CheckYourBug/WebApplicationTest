
url = "http://selenium1py.pythonanywhere.com/"
class BasePage():
    #метод init
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    def open(self):
        self.browser.get(self.url)