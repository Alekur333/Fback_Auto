from .base_page import BasePage
from .locators import SigninPageLocators, AppsFunctionsLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class SignInPage(BasePage):

    # def fill_and_submit_signin(self, mail, password):
    #     try:
    #         self.browser.find_element(*AppsFunctionsLocators.HELP_BUTTON_CLOSE).click
    #     except:
    #         self.should_be_signin_page(mail, password)

    def should_be_signin_page(self, mail, password):
        self.check_url_signin_page()
        self.signin_mail_field(mail)
        self.signin_password_field(password)
        self.signin_input_btn()

    # Проверяем переход на страницу входа
    def check_url_signin_page(self):
        WebDriverWait(self.browser, 10).until(ec.url_contains("signin"))
        assert "signin" in self.browser.current_url, 'Регистрация не прошла'

    # Заполняем обязательные поля и входим
    def signin_mail_field(self, mail):
        try:
            input1 = self.browser.find_element(*SigninPageLocators.MAIL_FIELD)
            result = True
            input1.send_keys(mail)
        except:
            result = False
        assert result == True, 'Поле "Электронная почта" не найдено'

    def signin_password_field(self, password):
        try:
            input2 = self.browser.find_element(*SigninPageLocators.PASSWORD_FIELD)
            result = True
            input2.send_keys(password)
        except:
            result = False
        assert result == True, 'Поле "Пароль" не найдено'

    # Входим в аккаунт
    def signin_input_btn(self):
        try:
            button2 = self.browser.find_element(*SigninPageLocators.SIGNIN_BTN)
            result = True
            button2.click()
        except:
            result = False
        assert result == True, 'Кнопка "Войти в аккаунт" не найдена'

    # Проверяем переход на страницу приложений после успешного входа
    def should_be_apps_page(self):
        WebDriverWait(self.browser, 10).until(ec.url_contains("apps"))
        assert "apps" in self.browser.current_url, 'Вход не совершен'

