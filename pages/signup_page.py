from .base_page import BasePage
from .locators import SignupPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class SignUpPage(BasePage):

    def should_be_signup_page(self, regname, mail, regphone):
        self.name_field_fill(regname)
        self.email_field_fill(mail)
        self.phone_field_fill(regphone)
        self.agree_button()
        self.create_button()

        # Заполняем Поле "Ваше имя"
    def name_field_fill(self, regname):
        try:
            name = self.browser.find_element(*SignupPageLocators.REG_NAIM_FIELD)
            result = True
            name.send_keys(regname)
        except:
            result = False
        assert result == True, 'Поле "Ваше имя" не найдено'

        # Поле "Ваш e-mail"
    def email_field_fill(self, mail):
        try:
            email = self.browser.find_element(*SignupPageLocators.REG_MAIL_FIELD)
            result = True
            email.send_keys(mail)
        except:
            result = False
        assert result == True, 'Поле "Ваш e-mail" не найдено или нет значения email'

        # Поле "Номер мобильного телефона"
    def phone_field_fill(self, regphone):
        try:
            phone = self.browser.find_element(*SignupPageLocators.REG_PHONE_FIELD)
            result = True
            phone.send_keys(regphone)
        except:
            result = False
        assert result == True, 'Поле "Номер мобильного телефона" не найдено'

    # Нажать чек-бокс «даю согласие»
    def agree_button(self):
        try:
            agree = self.browser.find_element(*SignupPageLocators.REG_AGREE_BTN)
            agree.click()
            result = True
        except:
            result = False
        assert result == True, "Чек-бокс согласия не найден"

        # Нажать кнопку "Создать аккаунт"
    def create_button(self):
        try:
            button1 = WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable((SignupPageLocators.REG_CREATE_BTN)))
            button1.click()
            result = True
        except:
            result = False
        assert result == True,  "Кнопка 'Создать аккаунт' не найдена"
        # time.sleep(2)
