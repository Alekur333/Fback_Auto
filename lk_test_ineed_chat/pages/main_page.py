from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class MainPage(BasePage):

    def should_be_user_menu(self):
        assert WebDriverWait(self.browser, 10).until \
            (ec.presence_of_element_located(MainPageLocators.USER_MENU_BTN)), \
            "Кнопка меню пользователя не найдена"

    def go_to_user_menu(self):
        self.browser.find_element(*MainPageLocators.USER_MENU_BTN).click()

    def should_be_profile_btn(self):
        assert WebDriverWait(self.browser, 10).until \
            (ec.presence_of_element_located(MainPageLocators.USER_MENU_PROFILE_BTN)), \
            "Кнопка 'Выйти' не найдена"

    def go_to_profile(self):
        self.browser.find_element(*MainPageLocators.USER_MENU_PROFILE_BTN).click()

    def should_be_logout_btn(self):
        assert WebDriverWait(self.browser, 10).until \
            (ec.presence_of_element_located(MainPageLocators.USER_MENU_LOGOUT_BTN)), \
            "Кнопка 'Выйти' не найдена"

    def make_logout(self):
        self.browser.find_element(*MainPageLocators.USER_MENU_LOGOUT_BTN).click()
