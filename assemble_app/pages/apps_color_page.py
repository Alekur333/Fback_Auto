from .base_page import BasePage
from .locators import AppsColorLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class AppsColorPage(BasePage):

    def set_apps_color(self):
        self.should_be_apps_color()
        self.select_apps_color()
        self.should_be_color_complete_btn()
        self.color_complete()

    def should_be_apps_color(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsColorLocators.APPS_COLOR)), \
            "Поле c цветом rgb(38, 166, 91) не найдено"

    def select_apps_color(self):
        self.browser.find_element(*AppsColorLocators.APPS_COLOR).click()

    def should_be_color_complete_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsColorLocators.COLOR_COMPLETE_BTN)), \
            "Кнопка Продолжить на странице цвета не найдена"

    def color_complete(self):
        self.browser.find_element(*AppsColorLocators.COLOR_COMPLETE_BTN).click()