from .base_page import BasePage
from .locators import CreateAppPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class CreateAppPage(BasePage):

    def should_be_create_app_btn(self):
        assert WebDriverWait(self.browser, 20).until\
            (ec.presence_of_element_located(CreateAppPageLocators.CREATE_APP_BTN)), \
            "Кнопка СОЗДАТЬ ПРИЛОЖЕНИЕ не найдена"

    def go_to_create_app_page(self):
        self.browser.find_element(*CreateAppPageLocators.CREATE_APP_BTN).click()

