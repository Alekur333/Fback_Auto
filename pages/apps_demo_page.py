from .base_page import BasePage
from .locators import AppsDemoLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class AppsDemoPage(BasePage):

    def demo_app_store_code(self):
        code = WebDriverWait(self.browser, 120).until\
            (ec.presence_of_element_located(AppsDemoLocators.DEMO_APPS_CODE)).text
        assert "demo" in self.browser.current_url, 'Страница сохранения Демо приложения не загрузилась'
        print(code)

    def should_be_demo_safe_btn(self):
        assert WebDriverWait(self.browser, 2).until\
            (ec.presence_of_element_located(AppsDemoLocators.DEMO_SAFE_BTN)), \
            "Кнопка Сохранить на странице Демо не найдена"

    def demo_safe_btn(self):
        self.browser.find_element(*AppsDemoLocators.DEMO_SAFE_BTN).click()

    def should_be_signin_btn_for_demo_app_on_popup_window(self):
        assert WebDriverWait(self.browser, 2).until\
            (ec.presence_of_element_located(AppsDemoLocators.DEMO_SIGNIN_BTN)), \
            "Кнопка ВОЙТИ в Демо не найдена"

    def signin_for_demo_app_on_popup_window(self):
        self.browser.find_element(*AppsDemoLocators.DEMO_SIGNIN_BTN).click()

    def should_be_signup_btn_for_demo_app_on_popup_window(self):
        assert WebDriverWait(self.browser, 2).until\
            (ec.presence_of_element_located(AppsDemoLocators.DEMO_SIGNUP_BTN)), \
            "Кнопка ВОЙТИ в Демо не найдена"

    def signup_for_demo_app_on_popup_window(self):
        self.browser.find_element(*AppsDemoLocators.DEMO_SIGNUP_BTN).click()

