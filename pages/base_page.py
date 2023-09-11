from selenium.common.exceptions import NoSuchElementException
import time
import math
import pyperclip
from selenium.common.exceptions import NoAlertPresentException
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
    def solve_and_get_code(self):
        #обращаемся к всплывающему окну
        alert = self.browser.switch_to.alert
        #находим значение, которое необходимо подставить с помощью сплит
        value = alert.text.split(" ")[2]
        print(value)
        answer = str(math.log(abs((12 * math.sin(float(value))))))
        print(answer)
        pyperclip.copy(answer)
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


