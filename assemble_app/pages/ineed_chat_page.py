from .base_page import BasePage
from .locators import IneedchatPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class IneedChatPage(BasePage):

    def should_be_main_menu_open_btn(self):
        assert WebDriverWait(self.browser, 2).until(ec.presence_of_element_located(IneedchatPageLocators.MAIN_MENU_OPEN)), \
            "Кнопка МЕНЮ не найдена"
        # assert self.is_element_present(*IneedchatPageLocators.MAIN_MENU_OPEN), "Кнопка МЕНЮ не найдена"

    def go_to_main_menu(self):
        self.browser.find_element(*IneedchatPageLocators.MAIN_MENU_OPEN).click()
        # entrance = WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable(IneedchatPageLocators.MAIN_MENU_OPEN))
        # entrance.click()

    def should_be_main_menu_close_btn(self):
        assert WebDriverWait(self.browser, 2).until(ec.presence_of_element_located(IneedchatPageLocators.MAIN_MENU_CLOSE)), \
            "Кнопка Закрыть МЕНЮ не найдена"

    def should_be_clients_entrance_btn_in_main_menu(self):
        assert WebDriverWait(self.browser, 2).until(ec.presence_of_element_located(IneedchatPageLocators.MAIN_MENU_CLIENTS_ENTRANCE)),\
            "Кнопка 'Вход для клиентов' не найдена"

    def go_to_clients_entrance_in_main_menu(self):
        self.browser.find_element(*IneedchatPageLocators.MAIN_MENU_CLIENTS_ENTRANCE).click()

