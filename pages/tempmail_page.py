from pages.base_page import BasePage
from .locators import TempmailPageLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import re

class TempMailPage(BasePage):

    # На странице временной почты взять мейл для регистрации
    def get_tempmail(self):
        tempmail = self.browser.find_element(*TempmailPageLocators.TEMPMAIL).text
        print(f'Ваш email для регистрации {tempmail}')
        return tempmail

    def get_letter_password(self, browser):
        # В окне почты проверить наличие письма и взять пароль
        try:
            letter = WebDriverWait(browser, 10).until(ec.presence_of_element_located((TempmailPageLocators.LETTER_PASSWORD)))
            letter_pass = letter.text
            temp_password = re.findall(r"<b>(\w+)", letter_pass)
            print(f'Ваш пароль для регистрации {temp_password}')
            return temp_password
            # result = True
        except:
            result = False
        assert result == True,  "Пароль из письма не получен"



