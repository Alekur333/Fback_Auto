from .base_page import BasePage
from .locators import LoginPageLocators, CompaniesPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):

    def should_be_login_page(self, phone, sms):
        self.check_url_login_page()
        self.should_be_phone_field(phone)
        self.should_be_get_sms_btn()
        # self.get_sms_btn()
        self.should_be_sms_field(sms)
        self.should_be_login_btn()
        # self.should_be_news_page()

    # Проверяем переход на страницу входа
    def check_url_login_page(self):
        WebDriverWait(self.browser, 10).until(ec.url_contains("login"))
        assert "login" in self.browser.current_url, 'Страница LOGIN не загрузилась'

    # Заполняем обязательные поля
    def should_be_phone_field(self, phone):
        try:
            input_phone = self.browser.find_element(*LoginPageLocators.PHONE_FIELD)
            result = True
            input_phone.send_keys(phone)
        except:
            result = False
        assert result == True, 'Поле "Номер телефона" не найдено'

    def should_be_get_sms_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(LoginPageLocators.GET_SMS_BTN)), \
            "Кнопка 'Отправить СМС' не найдена"
        self.browser.find_element(*LoginPageLocators.GET_SMS_BTN).click()

    def should_be_sms_field(self, sms):
        assert WebDriverWait(self.browser, 10).until \
            (ec.presence_of_element_located(LoginPageLocators.SMS_FIELD)), \
            "Поле 'Код доступа из СМС' не найдено"
        self.browser.find_element(*LoginPageLocators.SMS_FIELD).send_keys(sms)

    # Входим в аккаунт
    def should_be_login_btn(self):
        assert WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(LoginPageLocators.LOGIN_BTN)), \
            "Кнопка 'Отправить СМС' не найдена"
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).click()

    # Проверяем переход на страницу компаний
    def should_be_companies_page(self):
        assert WebDriverWait(self.browser, 10).until(ec.url_contains("companies")), 'Это не страница компаний'

    def should_be_company1(self):
        company1_must_be = (CompaniesPageLocators.COMPANY1_MUST_BE_NAME)
        try:
            company1_name = self.browser.find_element(*CompaniesPageLocators.COMPANY1_NAME).text
            print(f'Первая компания называется {company1_name}')
            assert company1_name == company1_must_be
            self.browser.find_element(*CompaniesPageLocators.COMPANY1_BTN).click()
        except:
            print(f'Компания {company1_must_be} не найдена')
            self.browser.find_element(*CompaniesPageLocators.COMPANY1_BTN).click()



