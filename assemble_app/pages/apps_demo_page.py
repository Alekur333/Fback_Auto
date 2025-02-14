from .base_page import BasePage
from .locators import AppsDemoLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class AppsDemoPage(BasePage):

    def demo_app_store_code(self):
        code = WebDriverWait(self.browser, 300).until\
            (ec.presence_of_element_located(AppsDemoLocators.DEMO_APPS_CODE)).text
        assert "demo" in self.browser.current_url, 'Страница сохранения Демо приложения не загрузилась'
        print(f"Код созданного Вами приложения {code}.")

    def should_be_demo_safe_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsDemoLocators.DEMO_SAFE_BTN)), \
            "Кнопка Сохранить на странице Демо не найдена"

    def demo_safe_btn(self):
        self.browser.find_element(*AppsDemoLocators.DEMO_SAFE_BTN).click()

    def should_be_signin_btn_for_demo_app_on_popup_window(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsDemoLocators.DEMO_SIGNIN_BTN)), \
            "Кнопка ВОЙТИ в Демо не найдена"

    def signin_for_demo_app_on_popup_window(self):
        self.browser.find_element(*AppsDemoLocators.DEMO_SIGNIN_BTN).click()

    def should_be_signup_btn_for_demo_app_on_popup_window(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsDemoLocators.DEMO_SIGNUP_BTN)), \
            "Кнопка ВОЙТИ в Демо не найдена"

    def should_be_grate_sign(self):
        self.browser.find_element(*AppsDemoLocators.DEMO_GRATE_SIGN).click()

    def signup_for_demo_app_on_popup_window(self):
        self.browser.find_element(*AppsDemoLocators.DEMO_SIGNUP_BTN).click()

    def should_be_close_popup_window_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsDemoLocators.DEMO_POPUP_WINDOW_CLOSE)), \
            "Кнопка ВОЙТИ в Демо не найдена"

    def close_popup_window(self):
        self.browser.find_element(*AppsDemoLocators.DEMO_POPUP_WINDOW_CLOSE).click()

    def should_be_signup_url_after_demo(self):
        assert WebDriverWait(self.browser, 30).until(ec.url_contains("signup")), \
            'Страница регистрации не доступна'
        # assert "signup" in self.browser.current_url, 'Страница регистрации не доступна'

