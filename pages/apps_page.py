from .base_page import BasePage
from .locators import AppDoneLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class AppsPage(BasePage):

    def should_be_remove_app_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppDoneLocators.REMOVE_APP_BTN)), \
            "Кнопка 'Демо приложение' не найдена"

    def remove_app(self):
        self.browser.find_element(*AppDoneLocators.REMOVE_APP_BTN).click()