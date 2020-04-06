from .base_page import BasePage
from .locators import AppDoneLocators, AppsFunctionsLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class AppsPage(BasePage):

    def should_be_remove_app_btn(self):
        # assert self.browser.find_element(*AppDoneLocators.REMOVE_APP_BTN).click(),\
        #     "Кнопка удалить 'Демо приложение' не найдена"
        # assert WebDriverWait(self.browser, 10).until\
        #     (ec.presence_of_element_located(AppDoneLocators.REMOVE_APP_BTN)), \
        #     "Кнопка удалить 'Демо приложение' не найдена"
        assert WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppDoneLocators.REMOVE_APP_BTN)), \
            "Кнопка удалить 'Демо приложение' не найдена, возможно приложение не собрано"


    # def remove_app(self):
    #     self.browser.find_element(*AppDoneLocators.REMOVE_APP_BTN).click()
    def remove_app(self):
        self.browser.find_element(*AppDoneLocators.REMOVE_APP_BTN).click()
        # try:
        #     WebDriverWait(self.browser, 3).until\
        #         (ec.element_to_be_clickable(AppsFunctionsLocators.HELP_BUTTON_CLOSE)).click.\
        #         find_element(*AppDoneLocators.REMOVE_APP_BTN).click()
        # except:
        #     self.browser.find_element(*AppDoneLocators.REMOVE_APP_BTN).click()

    def should_be_remove_app_continue_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppDoneLocators.REMOVE_APP_CONTINUE_BTN)), \
            "Кнопка 'Демо приложение' не найдена"

    def remove_app_continue_btn(self):
        self.browser.find_element(*AppDoneLocators.REMOVE_APP_CONTINUE_BTN).click()
